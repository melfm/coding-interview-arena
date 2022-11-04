"""
Linear Regression - Derive the closed form solution and implement it.
"""
import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(42)
X = np.random.randn(500, 1)
# Linear function of the input
y = 2 * X + 1 + 1.2 * np.random.randn(500, 1)
print("Input shape: ", X.shape, y.shape)


def find_W(X, y):
    m = X.shape[0]
    # append one extra dim for the bias term
    # the bias/intercept is included with W in this
    # formulation - I'm not sure if it can be calculated
    # separately?
    X = np.append(X, np.ones((m, 1)), axis=1)
    # reshape y to (m, 1)
    y = y.reshape(m, 1)
    # The Normal Equation
    # This parameter includes the slope and intercept
    W = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, y))
    return W


def predict(W, X):
    m = X.shape[0]
    X = np.append(X, np.ones((m, 1)), axis=1)
    preds = np.dot(X, W)
    return preds


fig = plt.figure(figsize=(8, 6))
plt.plot(X, y, 'b.')
W = find_W(X, y)
preds = predict(W, X)

plt.plot(X, preds, 'c-')
plt.xlabel('X - Input')
plt.ylabel('y - target / true')
plt.show()
