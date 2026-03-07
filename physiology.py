import numpy as np

class CardiacModel:

    def __init__(self):

        self.hr = 75
        self.cycle = 60 / self.hr

        self.EDV = 120
        self.ESV = 50
        self.SV = self.EDV - self.ESV

        self.iso_c = 0.1
        self.eject = 0.3
        self.iso_r = 0.1
        self.fill = 0.3

        self.radius = 0.01
        self.area = np.pi * self.radius**2

        self.rho = 1060
        self.mu = 0.0035


    def phase(self,t):
        return t % self.cycle


    def volume(self,t):

        p = self.phase(t)

        if p < self.iso_c:
            return self.EDV

        elif p < self.iso_c + self.eject:
            return self.EDV - self.SV*(p-self.iso_c)/self.eject

        elif p < self.iso_c + self.eject + self.iso_r:
            return self.ESV

        else:
            return self.ESV + self.SV*(p-self.iso_c-self.eject-self.iso_r)/self.fill


    def pressure(self,t):

        p = self.phase(t)

        if p < self.iso_c:
            return 10 + 110*(p/self.iso_c)

        elif p < self.iso_c + self.eject:
            return 120 - 20*(p-self.iso_c)/self.eject

        elif p < self.iso_c + self.eject + self.iso_r:
            return 100*(1-(p-self.iso_c-self.eject)/self.iso_r)

        else:
            return 10 + 5*(p-self.iso_c-self.eject-self.iso_r)/self.fill


    def inlet_velocity(self,t):

        p = self.phase(t)

        if p < self.iso_c:
            Q = 0

        elif p < self.iso_c + self.eject:

            x = (p-self.iso_c)/self.eject
            Q = (self.SV*1e-6/self.eject)*np.sin(np.pi*x)

        else:
            Q = 0

        return Q/self.area


    def reynolds(self,v):

        D = 2*self.radius
        return self.rho*v*D/self.mu


    def shear(self,v):

        return 4*self.mu*v/self.radius