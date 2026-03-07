import numpy as np

class FlowSolver:

    def __init__(self, cardiac):

        self.cardiac = cardiac

        self.dt = 0.02
        self.time = 0

        self.n_particles = 250

        self.x = np.random.rand(self.n_particles)
        self.y = np.random.uniform(-0.3,0.3,self.n_particles)

        self.vel_history=[]
        self.Re_history=[]
        self.shear_history=[]

        # velocity field grid
        self.grid_x,self.grid_y=np.meshgrid(
            np.linspace(0,1,40),
            np.linspace(-0.3,0.3,30)
        )


    def velocity_field(self,v):

        u = v*np.exp(-5*self.grid_y**2)
        w = np.zeros_like(u)

        return u,w


    def step(self):

        v = self.cardiac.inlet_velocity(self.time)

        dx = v*self.dt*5

        self.x += dx
        self.x[self.x>1] = 0

        self.vel_history.append(v)

        Re = self.cardiac.reynolds(v)
        tau = self.cardiac.shear(v)

        self.Re_history.append(Re)
        self.shear_history.append(tau)

        self.time += self.dt

        return v