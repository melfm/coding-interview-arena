"""
Optimization and gradient related Questions.
"""
import numpy as np


class C:
    """Consider the following class with the update function.
    Explain what it's calculating (what is the value of m and
    v at k time step?). Where would this be used in the
    context of optimization?
    See: https://towardsdatascience.com/adam-latest-trends-in-deep-learning-optimization-6be9a291375c
    See: https://cs231n.github.io/neural-networks-3/#ada
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
        self.m = self.d1 * self.m + (1 - self.d1) * x
        self.v = self.d2 * self.v + (1 - self.d2) * x * x

    def compute_gradient(self):
        pass

    def update(self, x, y):
        # pseudo-code with Bias correction
        step_size = 1
        epsilon = 0
        num_iterations = 100
        for iter in range(num_iterations):
            g = self.compute_gradient(x, y)
            m = self.d1 * m + (1 - self.d1) * g
            v = self.d2 * v + (1 - self.d2) * np.power(g, 2)
            m_hat = m / (1 - np.power(self.d1, iter))
            v_hat = v / (1 - np.power(self.d2, iter))
            w = w - step_size * m_hat / (np.sqrt(v_hat) + epsilon)