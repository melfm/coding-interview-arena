"""
Linear Regression - Implement using gradient descent.
For a slightly different LR using covariance calculation see:
https://machinelearningmastery.com/implement-simple-linear-regression-scratch-python/
"""
import numpy as np
import matplotlib.pyplot as plt


class LinearRegression():

    def __init__(self, learning_rate, iterations):
        self.learning_rate = learning_rate
        self.iterations = iterations

    def fit(self, X, y):

        self.m, self.n = X.shape
        # weight init
        self.W = np.zeros(self.n)
        self.b = 0
        self.X = X
        self.y = y

        # gradient descent steps
        for _ in range(self.iterations):
            self.update_W()

    def update_W(self):
        y_pred = self.predict(self.X)
        # calculate gradients
        # here we apply the chain rule to the MSE
        # (W^T.X - y)^2
        # recall: partial_derivative = 2 * (expression) * grad(expression)
        # this becomes X.(error_term)
        dW = -(2 * (self.X.T).dot(self.y - y_pred)) / self.m
        db = -2 * sum(self.y - y_pred) / self.m
        # update weights
        self.W = self.W - self.learning_rate * dW
        self.b = self.b - self.learning_rate * db

    def predict(self, X):
        return np.dot(X, self.W) + self.b


# Generate random data
np.random.seed(42)
X = np.random.randn(500, 1)
y = 2 * X + 1 + 1.2 * np.random.randn(500, 1)
print("Input shape: ", X.shape, y.shape)

LR = LinearRegression(0.0001, 10000)
LR.fit(X, y)
preds = LR.predict(X)

fig = plt.figure(figsize=(8, 6))
plt.plot(X, y, 'b.')
plt.plot(X, preds, 'c-')
plt.xlabel('X - Input')
plt.ylabel('y - target / true')
plt.show()
