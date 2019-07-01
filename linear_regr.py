import numpy as np

# Let's have y = mx + b
# so we have set of pairs (x,y) so we need calculate m and b
# m = (N * sum(xy) - sum(x) * sum(y)) / (N * sum(x**2) - (sum(x))**2))
# b = (sum(y) - m * sum(x)) / N
class LinearRegression:
    def __init__(self, values):
        self.y = np.array(values)
        self.x = np.array([number for number in range(1, len(values)+1)])
        self.values_to_return = []

    def getlinear(self, x1):
    
        self.m = (len(self.x) * np.sum(self.x*self.y) - np.sum(self.x) * np.sum(self.y)) / (len(self.x)*np.sum(self.x*self.x) - np.sum(self.x) * np.sum(self.x))
        self.b = (np.sum(self.y) - self.m*np.sum(self.x)) / len(self.x)

        return self.m * x1 + self.b

    def return_values_of_linear_regression(self):
        for x_param in self.x:
            self.values_to_return.append(self.getlinear(x_param))

        return self.values_to_return
