import seaborn as sns
import numpy as np
from numpy.random import uniform

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


def euclidean(point, data):
    return np.sqrt(np.sum((point - data)**2, axis=1))


class kMeans:

    def __init__(self, n_cluster=8, max_iter=300):
        self.n_cluster = n_cluster
        self.max_iter = max_iter

    def fit(self, x_train):

        # Randomly select centroid points, uniformly distributed
        min_, max_ = np.min(x_train, axis=0), np.max(x_train, axis=0)
        self.centroids = [uniform(min_, max_) for _ in range(self.n_cluster)]

        # Iterate, adjust centroids
        iter = 0

        prev_centroids = None
        while np.not_equal(self.centroids, prev_centroids).any() and \
            iter < self.max_iter:

            # Sort each datapoint, assigning to nearest centroid
            sorted_points = [[] for _ in range(self.n_cluster)]
            for x in x_train:
                dists = euclidean(x, self.centroids)
                centroid_idx = np.argmin(dists)
                sorted_points[centroid_idx].append(x)

            # Re-assign centroids
            prev_centroids = self.centroids
            self.centroids = [
                np.mean(cluster, axis=0) for cluster in sorted_points
            ]

            for i, centroid in enumerate(self.centroids):
                if np.isnan(centroid).any():
                    # Catch any nans resulting from centroids without
                    # any points.
                    self.centroids[i] = prev_centroids[i]

            iter += 1

    def evaluate(self, x):
        centroids = []
        centroid_idxs = []

        for xp in x:
            dists = euclidean(xp, self.centroids)
            centroid_idx = np.argmin(dists)
            centroids.append(self.centroids[centroid_idx])
            centroid_idxs.append(centroid_idx)

        return centroids, centroid_idx


def main():
    centers = 5
    X_train, true_labels = make_blobs(n_samples=100,
                                      centers=centers,
                                      random_state=42)
    X_train = StandardScaler().fit_transform(X_train)
    sns.scatterplot(x=[X[0] for X in X_train],
                    y=[X[1] for X in X_train],
                    hue=true_labels,
                    palette="deep",
                    legend=None)

    kmeans = kMeans(n_cluster=centers)
    kmeans.fit(X_train)
    plt.plot(
        [x for x, _ in kmeans.centroids],
        [y for _, y in kmeans.centroids],
        '+',
        markersize=10,
    )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


if __name__ == '__main__':
    main()
