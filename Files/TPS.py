import numpy as np

### Thin Plate Spline (TPS)
class TPS:
    def __init__(self, degree, b, x_values, y_values):
        self.a = degree
        self.b = b
        self.x_values = x_values
        self.y_values = y_values
        self.CentresX, self.CentresY = self.calcCentres()

    def calcCentres(self):
        # In the mean time, just use the point values as the centres
        CentresX = self.x_values
        CentresY = self.y_values
        return CentresX, CentresY

    def calcr(self, xc, x, yc, y):
        return np.sqrt(np.power((x - xc), 2) + np.power((y - yc), 2)) 

    def calcTPS(self, xc, x, yc, y):
            if(xc == x and yc == y):
                return 0
            r = self.calcr(xc, x, yc, y)
            return self.b * np.power(r, 2*self.a) * np.log(self.b * r)
    
    def DevcalcTPS(self, xc, x):
        if(xc == x):
            return 0
        r = self.calcr(xc, x, 0, 0)
        dIdr = self.b * np.power(r, 2*self.a-1) * (2*self.a*np.log(self.b*r)+1)
        return dIdr * (x - xc) / r
    
    def Dev2calcTPS(self, xc, x):
        if(xc == x):
            return 0
        r = self.calcr(xc, x, 0, 0)
        dIdr = self.b * np.power(r, 2*self.a-1) * (2*self.a*np.log(self.b*r)+1)
        d2Idr2 = self.b*np.power(r, 2*self.a-2)*(2*self.a*(2*self.a-1)*np.log(self.b*r)+4*self.a-1)
        return d2Idr2*np.power((x-xc)/r, 2) + dIdr*(1/r-(np.power((x-xc), 2)/np.power(r, 3)))
    
    def matrix_A(self):
        A = np.empty((len(self.x_values), len(self.CentresX)))
        for i in range(len(self.x_values)):
            for j in range(len(self.CentresX)):
                A[i, j] = self.calcTPS(self.CentresX[j], self.x_values[i], self.CentresY[j], self.y_values[i])
        return A

    def interpolate(self, w, x, y):
        n = len(self.CentresX)
        result = 0.0
        for i in range(n):
            result += w[i] * self.calcTPS(self.CentresX[i], x, self.CentresY[i], y)
        return result
    
    def interpolateDerivateX(self, w, x):
        n = len(self.CentresX)
        result = 0.0
        for i in range(n):
            result += w[i] * self.DevcalcTPS(self.CentresX[i], x)
        return result
    
    def interpolateDerivateY(self, w, y):
        n = len(self.CentresY)
        result = 0.0
        for i in range(n):
            result += w[i] * self.DevcalcTPS(self.CentresY[i], y)
        return result
    
    def interpolateDerivate2X(self, w, x):
        n = len(self.CentresX)
        result = 0.0
        for i in range(n):
            result += w[i] * self.Dev2calcTPS(self.CentresX[i], x)
        return result
    
    def interpolateDerivate2Y(self, w, y):
        n = len(self.CentresY)
        result = 0.0
        for i in range(n):
            result += w[i] * self.Dev2calcTPS(self.CentresX[i], y)
        return result