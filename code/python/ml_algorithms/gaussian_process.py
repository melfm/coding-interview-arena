import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.optimize import Bounds
from pyDOE import lhs
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline


class GaussianProcess:
    """Initializes a Gaussian Process model.

    Input:
    ------
    n_restarts: number of restarts of the local optimizer
    optimizer: optimizer algorithm
    """

    def __init__(self, n_restarts, optimizer):

        self.n_restarts = n_restarts
        self.optimizer = optimizer

    def correlation(self, x1, x2, theta):
        """Constructs the correlation matrix between X1 and X2.

        Input:
        -----
        x1, x2: 2D arrays, (n_samples, n_features)
        theta: array, correlation legnths for different dimensions

        Output:
        ------
        K: the correlation matrix
        """
        K = np.zeros((x1.shape[0], x2.shape[0]))

        for i in range(x1.shape[0]):
            K[i, :] = np.exp(-np.sum(theta * (x1[i, :] - x2)**2, axis=1))

        return K

    def negLikelihood(self, theta):
        """Negative likelihood function.

        Input
        -----
        theta: array, logarithm of the correlation legnths for different dimensions
        
        Output
        ------
        LnLike: likelihood value
        """

        # Correlation length
        theta = 10**theta
        n = self.X.shape[0]

        ones = np.ones((n, 1))

        # Construct correlation matrix
        # adding nugget term to the diagonal of K
        K = self.correlation(self.X, self.X, theta) + np.eye(n) * 1e-10
        inv_K = np.linalg.inv(K)

        # Mean estimation
        mu = (ones.T @ inv_K @ self.y) / (ones.T @ inv_K @ ones)

        # Variance estimation
        sigmaSqr = (self.y - mu * ones).T @ inv_K @ (self.y - mu * ones) / n

        # Compute likelihood
        detK = np.linalg.det(K)

        lnLikelihood = -(n / 2) * np.log(sigmaSqr) - 0.5 * np.log(detK)

        # update the attributes
        self.K, self.inv_K, self.mu, self.sigmaSqr = K, inv_K, mu, sigmaSqr

        return -lnLikelihood.flatten()

    def fit(self, X, y):
        """GP model training
        
        Input
        -----
        X: 2D array of shape (n_samples, n_features)
        y: 2D array of shape (n_samples, 1)
        """

        self.X, self.y = X, y
        lb, ub = -3, 2

        # Generate random starting points (Latin Hypercube)
        lhd = lhs(self.X.shape[1], samples=self.n_restarts)

        # Scale random samples to the given bounds
        initial_points = (ub - lb) * lhd + lb

        # Create A Bounds instance for optimization
        bnds = Bounds(lb * np.ones(X.shape[1]), ub * np.ones(X.shape[1]))

        # Run local optimizer on all points
        opt_para = np.zeros((self.n_restarts, self.X.shape[1]))
        opt_func = np.zeros((self.n_restarts, 1))
        for i in range(self.n_restarts):
            res = minimize(self.negLikelihood,
                           initial_points[i, :],
                           method=self.optimizer,
                           bounds=bnds)
            opt_para[i, :] = res.x
            opt_func[i, :] = res.fun

        # Locate the optimum results
        self.theta = opt_para[np.argmin(opt_func)]

        # Update attributes
        self.negLnlike = self.negLikelihood(self.theta)

    def predict(self, X_test):
        """GP model predicting
        
        Input
        -----
        X_test: test set, array of shape (n_samples, n_features)
        
        Output
        ------
        f: GP predictions
        SSqr: Prediction variances"""

        n = self.X.shape[0]
        one = np.ones((n, 1))

        # Construct correlation matrix between test and train data
        k = self.correlation(self.X, X_test, 10**self.theta)

        # Mean prediction
        f = self.mu + k.T @ self.inv_K @ (self.y - self.mu * one)

        # Variance prediction
        SSqr = self.sigmaSqr * (1 - np.diag(k.T @ self.inv_K @ k))

        return f.flatten(), SSqr.flatten()

    def score(self, X_test, y_test):
        """Calculate root mean squared error
        
        Input
        -----
        X_test: test set, array of shape (n_samples, n_features)
        y_test: test labels, array of shape (n_samples, )
        
        Output
        ------
        RMSE: the root mean square error"""

        y_pred, SSqr = self.predict(X_test)
        RMSE = np.sqrt(np.mean((y_pred - y_test)**2))

        return RMSE


def Test_1D(X):
    """1D Test Function"""

    y = (X * 6 - 2)**2 * np.sin(X * 12 - 4)

    return y


def Test_2D(X):
    """2D Test Function"""

    y = (1 - X[:, 0])**2 + 100 * (X[:, 1] - X[:, 0]**2)**2

    return y


run_1d = False

if run_1d:
    ##########
    # 1D Case
    ##########
    # Training data
    #import pdb;pdb.set_trace()
    X_train = np.array([0.0, 0.1, 0.2, 0.4, 0.5, 0.6, 0.8, 1], ndmin=2).T
    y_train = Test_1D(X_train)

    # Testing data
    X_test = np.linspace(0.0, 1, 100).reshape(-1, 1)
    y_test = Test_1D(X_test)

    # GP model training
    GP = GaussianProcess(n_restarts=10, optimizer='L-BFGS-B')
    GP.fit(X_train, y_train)

    # GP model predicting
    y_pred, y_pred_SSqr = GP.predict(X_test)


    fig, ax = plt.subplots(figsize=(7,5))

    X = np.linspace(0.0, 1, 100).reshape(-1,1)
    y = Test_1D(X)

    ax.plot(X, y,'r--', lw=2)
    ax.tick_params(axis='both', which='major', labelsize=12)
    ax.set_xlabel('x', fontsize=15)
    ax.set_ylabel('f(x)', fontsize=15)
    ax.set_ylim([-10,20]);
    plt.savefig('images/Test_1D')

    fig, ax = plt.subplots(figsize=(7,5))
    ax.plot(X_test,y_test,'r--',linewidth=2,label='Test Function')
    ax.plot(X_train,y_train,'ro',markerfacecolor='r', markersize=10, label='Training Data')
    ax.plot(X_test,y_pred,'b-', lw=2, label='GP Prediction')
    ax.fill_between(X_test.flatten(), y_pred-1.96*np.sqrt(y_pred_SSqr), 
                    y_pred+1.96*np.sqrt(y_pred_SSqr),
                    facecolor='lavender',label='95% Credibility Interval')
    ax.tick_params(axis='both', which='major', labelsize=12)
    ax.set_xlabel('x', fontsize=15)
    ax.set_ylabel('f(x)', fontsize=15)
    ax.set_ylim([-10,20])
    ax.legend(loc="upper left",prop={'size': 12});
    plt.savefig('images/Test_1D_results')


else:
    ##########
    # 2D Case
    ##########

    # Training data
    sample_num = 25
    lb, ub = np.array([-2, -1]), np.array([2, 3])
    X_train = (ub - lb) * lhs(2, samples=sample_num) + lb
    y_train = Test_2D(X_train).reshape(-1, 1)

    # Test data
    X1 = np.linspace(-2, 2, 20)
    X2 = np.linspace(-1, 3, 20)
    X1, X2 = np.meshgrid(X1, X2)
    X_test = np.hstack((X1.reshape(-1, 1), X2.reshape(-1, 1)))
    y_test = Test_2D(X_test)

    # GP model training
    pipe = Pipeline([('scaler', MinMaxScaler()),
                     ('GP', GaussianProcess(n_restarts=10,
                                            optimizer='L-BFGS-B'))])
    pipe.fit(X_train, y_train)

    # GP model predicting
    y_pred, y_pred_SSqr = pipe.predict(X_test)

    # Accuracy score
    pipe.score(X_test, y_test)

    # Visualizing the test function
    fig, ax = plt.subplots(figsize=(7,5))
    h = ax.contourf(X1, X2, y_test.reshape(20,-1), levels=15, cmap='GnBu')
    ax.set_xlabel(r'$x_1$', fontsize=15)
    ax.set_ylabel(r'$x_2$', fontsize=15)
    plt.colorbar(h)
    plt.savefig('images/Test_2D')

    # Training data
    sample_num = 25
    lb, ub = np.array([-2, -1]), np.array([2, 3])
    X_train = (ub-lb)*lhs(2, samples=sample_num) + lb

    # Compute labels
    y_train = Test_2D(X_train).reshape(-1,1)


    # Vislauzing training samples
    fig, ax = plt.subplots(figsize=(7,5))
    ax.scatter(X_train[:,0], X_train[:,1], c='r', label='Training Data')
    ax.set_xlabel(r'$x_1$', fontsize=15)
    ax.set_ylabel(r'$x_2$', fontsize=15)
    ax.legend(loc="upper left",prop={'size': 12})
    plt.savefig('images/Test_2D_samples')


    # Post-processing - Contour plot
    fig, ax = plt.subplots(1, 2, figsize=(10,4))
    title = ['True Function', 'GP Approximation']
    display_y = [y_test, y_pred]

    for i in range(2):
        h = ax[i].contourf(X_test[:,0].reshape(20,-1), 
                    X_test[:,1].reshape(20,-1), 
                    display_y[i].reshape(20,-1), levels=15, cmap='GnBu');
        ax[i].set_xlabel(r'$x_1$', fontsize=15)
        ax[i].set_ylabel(r'$x_2$', fontsize=15)
        ax[i].set_title(title[i], fontsize=15)
        fig.colorbar(h, ax=ax[i])
    plt.tight_layout()
    plt.savefig('images/Test_2D_results')