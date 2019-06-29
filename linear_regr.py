import numpy

# I'm using idea from https://devarea.com/linear-regression-with-numpy/#.XRfdcegzaUk
class LinearRegression:
    def __init__(self, values):
        
        self.y = numpy.array(values)
        self.x = numpy.array([number for number in range(1, len(values)+1)])

    def getlinear(self):
 
        def inner(x1):
            return self.m * x1 + self.b
    
        self.m = (len(self.x) * numpy.sum(self.x*self.y) - numpy.sum(self.x) * numpy.sum(self.y)) / (len(self.x)*numpy.sum(self.x*self.x) - numpy.sum(self.x) * numpy.sum(self.x))
        self.b = (numpy.sum(self.y) - self.m*numpy.sum(self.x)) / len(self.x)
        return inner