"""
Logistic Regression for a binary classification task.
Using the data under data/marks_binary_class.txt
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.linear_model import LogisticRegression
from scipy.optimize import fmin_tnc
from sklearn.metrics import accuracy_score


def load_data(path, header):
    marks_df = pd.read_csv(path, header=header)
    return marks_df


class LogisticRegressionGD():

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def fit(self, x, y, theta):
        self.m = x.shape[0]
        opt_weights = fmin_tnc(func=self.cost_function,
                               x0=theta,
                               fprime=self.gradient,
                               args=(x, y.flatten()))
        self.w_ = opt_weights[0]
        return self

    def predict(self, x):
        theta = self.w_[:, np.newaxis]
        return self.probability(theta, x)

    def probability(self, theta, x):
        return self.sigmoid(np.dot(x, theta))

    def cost_function(self, theta, x, y):
        total_cost = -(1 / self.m) * np.sum(
            y * np.log(self.probability(theta, x)) +
            (1 - y) * np.log(1 - self.probability(theta, x)))

        return total_cost

    def gradient(self, theta, x, y):
        return (1 / self.m) * np.dot(X.T, self.sigmoid(np.dot(x, theta)) - y)

    def accuracy(self, x, true_label, probab_threshold=0.5):
        predicted_classes = (self.predict(x) >= probab_threshold).astype(int)
        predicted_classes = predicted_classes.flatten()
        accuracy = np.mean(predicted_classes == true_label)
        return accuracy * 100


if __name__ == "__main__":
    data = load_data("data/marks_binary_class.txt", None)

    # X = feature values, all the columns except the last column
    X = data.iloc[:, :-1]

    # y = target values, last column of the data frame
    y = data.iloc[:, -1]

    # filter out the applicants that got admitted
    admitted = data.loc[y == 1]

    # filter out the applicants that din't get admission
    not_admitted = data.loc[y == 0]

    # plots
    plt.scatter(admitted.iloc[:, 0],
                admitted.iloc[:, 1],
                s=10,
                label='Admitted')
    plt.scatter(not_admitted.iloc[:, 0],
                not_admitted.iloc[:, 1],
                s=10,
                label='Not Admitted')

    model = LogisticRegressionGD()

    # Prepare the data
    # Why do we need this extra column of 1s here?
    # without it, the accuracy is lower!
    X = np.c_[np.ones((X.shape[0], 1)), X]
    y = y[:, np.newaxis]
    theta = np.zeros((X.shape[1], 1))

    model.fit(X, y, theta)
    predicted_classes = model.predict(X)
    accuracy = model.accuracy(X, y.flatten())
    parameters = model.w_
    print("The accuracy of the model is {}".format(accuracy))
    print("The model parameters using Gradient descent")
    print("\n")
    print(parameters)

    x_values = [np.min(X[:, 1] - 2), np.max(X[:, 2] + 2)]
    y_values = - (parameters[0] + np.dot(parameters[1], x_values)) / parameters[2]

    plt.plot(x_values, y_values, label='Decision Boundary')
    plt.xlabel('Marks in 1st Exam')
    plt.ylabel('Marks in 2nd Exam')
    plt.legend()
    plt.show()

    # Using scikit-learn
    model = LogisticRegression()
    model.fit(X, y)
    parameters = model.coef_
    predicted_classes = model.predict(X)
    accuracy = accuracy_score(y.flatten(),predicted_classes)
    print('The accuracy score using scikit-learn is {}'.format(accuracy))
    print("The model parameters using scikit learn")
    print(parameters)