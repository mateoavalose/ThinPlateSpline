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

    def calcTPS(self, xc, x):
            if(xc == x):
                return 0
            r = np.sqrt(np.power((xc - x), 2))
            return self.b * np.power(r, 2*self.a) * np.log(self.b * r)
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