
"""
Optimization and gradient related Questions.
"""

class C:
    """Consider the following class with the update function.
    Explain what it's calculating (what is the value of m and
    v at k time step?). Where would this be used in the
    context of optimization?
    See: https://towardsdatascience.com/adam-latest-trends-in-deep-learning-optimization-6be9a291375c
    """

    def __init__(self, d1, d2):

        self.d1 = d1
        self.d2 = d2
        self.m = 0
        self.v = 0

    def update(self, x):
        # The first moment is mean, and the
        # second moment is uncentered variance
        # m and v are moving averages.
        self.m = self.d1 * self.m + (1-self.d1)*x
        self.v = self.d2 * self.v + (1-self.d2)*x*x