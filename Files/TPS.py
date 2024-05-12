import numpy as np

### Thin Plate Spline (TPS)
class TPS:
    def __init__(self, degree, b, x_values):
        self.a = degree
        self.b = b
        self.x_values = x_values
        self.Centres = self.calcCentres()

    def calcCentres(self):
        # In the mean time, just use the x values as the centres
        Centres = self.x_values
        return Centres
    
    def calcr(self, xc, x):
        return np.sqrt(np.power((x - xc), 2)) 
    
    def calcTPS(self, xc, x):
        if(xc == x):
            return 0
        r = self.calcr(xc, x)
        return self.b * np.power(r, 2*self.a) * np.log(self.b * r)
    
    def DevcalcTPS(self, xc, x):
        if(xc == x):
            return 0
        r = self.calcr(xc, x)
        dIdr = self.b * np.power(r, 2*self.a-1) * (2*self.a*np.log(self.b*r)+1)
        return dIdr * (x - xc) / r
    
    def Dev2calcTPS(self, xc, x):
        if(xc == x):
            return 0
        r = self.calcr(xc, x)
        dIdr = self.b * np.power(r, 2*self.a-1) * (2*self.a*np.log(self.b*r)+1)
        d2Idr2 = self.b*np.power(r, 2*self.a-2)*(2*self.a*(2*self.a-1)*np.log(self.b*r)+4*self.a-1)
        return d2Idr2*np.power((x-xc)/r, 2) + dIdr*(1/r-(np.power((x-xc), 2)/np.power(r, 3)))

    def matrix_A(self):
        A = np.empty((len(self.x_values), len(self.Centres)))
        for i in range(len(self.x_values)):
            for j in range(len(self.Centres)):
                A[i, j] = self.calcTPS(self.Centres[j], self.x_values[i])
        return A

    def interpolate(self, w, x):
        n = len(self.Centres)
        result = 0.0
        for i in range(n):
            result += w[i] * self.calcTPS(self.Centres[i], x)
        return result
    
    def interpolateDerivate(self, w, x):
        n = len(self.Centres)
        result = 0.0
        for i in range(n):
            result += w[i] * self.DevcalcTPS(self.Centres[i], x)
        return result
    
    def interpolateDerivate2(self, w, x):
        n = len(self.Centres)
        result = 0.0
        for i in range(n):
            result += w[i] * self.Dev2calcTPS(self.Centres[i], x)
        return result