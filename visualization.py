import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Visualizer:

    def __init__(self,solver):

        self.solver=solver

        self.fig=plt.figure(figsize=(14,8))

        self.ax_flow=plt.subplot(231)
        self.ax_stream=plt.subplot(232)
        self.ax_pv=plt.subplot(233)

        self.ax_vel=plt.subplot(234)
        self.ax_re=plt.subplot(235)
        self.ax_shear=plt.subplot(236)

        # particle animation
        self.scatter=self.ax_flow.scatter(
            solver.x,solver.y,
            c="red",s=10
        )

        self.ax_flow.set_title("Pulsatile Blood Particles")
        self.ax_flow.set_xlim(0,1)
        self.ax_flow.set_ylim(-0.35,0.35)
        self.ax_flow.grid(True)

        # streamline plot
        self.stream=self.ax_stream.streamplot(
            solver.grid_x,
            solver.grid_y,
            np.zeros_like(solver.grid_x),
            np.zeros_like(solver.grid_x),
            color="blue"
        )

        self.ax_stream.set_title("Velocity Streamlines")

        # PV loop
        self.V=[]
        self.P=[]
        self.pv_line,=self.ax_pv.plot([],[],"purple")

        self.ax_pv.set_xlim(40,130)
        self.ax_pv.set_ylim(0,130)
        self.ax_pv.set_title("Pressure-Volume Loop")

        # waveform plots
        self.vel_line,=self.ax_vel.plot([],[],"green")
        self.re_line,=self.ax_re.plot([],[],"orange")
        self.shear_line,=self.ax_shear.plot([],[],"red")

        self.ax_vel.set_title("Velocity")
        self.ax_re.set_title("Reynolds Number")
        self.ax_shear.set_title("Wall Shear Stress")


    def update(self,frame):

        v=self.solver.step()

        # particles
        self.scatter.set_offsets(
            np.c_[self.solver.x,self.solver.y]
        )

        # streamline update
        u,w=self.solver.velocity_field(v)

        self.ax_stream.clear()
        self.ax_stream.streamplot(
            self.solver.grid_x,
            self.solver.grid_y,
            u,w,
            color=u,
            cmap="plasma"
        )
        self.ax_stream.set_title("Velocity Streamlines")

        # PV loop
        t=self.solver.time

        vol=self.solver.cardiac.volume(t)
        pres=self.solver.cardiac.pressure(t)

        self.V.append(vol)
        self.P.append(pres)

        self.pv_line.set_data(self.V,self.P)

        # waveforms
        x=np.arange(len(self.solver.vel_history))

        self.vel_line.set_data(x,self.solver.vel_history)
        self.re_line.set_data(x,self.solver.Re_history)
        self.shear_line.set_data(x,self.solver.shear_history)

        self.ax_vel.set_xlim(0,len(x)+1)
        self.ax_re.set_xlim(0,len(x)+1)
        self.ax_shear.set_xlim(0,len(x)+1)

        return self.scatter,self.pv_line


    def animate(self):

        anim=FuncAnimation(
            self.fig,
            self.update,
            frames=800,
            interval=40
        )

        plt.tight_layout()
        plt.show()