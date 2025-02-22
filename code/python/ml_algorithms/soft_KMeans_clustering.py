import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

def soft_kmeans(X, K, beta=1.0, max_iters=100, tol=1e-4):
    """Soft K-Means Clustering Implementation (Non-Vectorized)"""
    N, D = X.shape
    
    # Initialize cluster centers randomly
    C = X[np.random.choice(N, K, replace=False)]
    
    for _ in range(max_iters):
        # Compute responsibilities (soft assignments)
        weights = np.zeros((N, K))
        for i in range(N):
            for k in range(K):
                distances = np.linalg.norm(X[i] - C[k])**2
                weights[i, k] = np.exp(-beta * distances)
            weights[i] /= weights[i].sum()
        
        # Update cluster centers
        new_C = np.zeros((K, D))
        for k in range(K):
            numerator = np.zeros(D)
            denominator = 0
            for i in range(N):
                numerator += weights[i, k] * X[i]
                denominator += weights[i, k]
            new_C[k] = numerator / denominator if denominator > 0 else C[k]
        
        # Check for convergence
        if np.linalg.norm(new_C - C) < tol:
            break
        C = new_C
    
    return C, weights

# Generate synthetic data
X, _ = make_blobs(n_samples=300, centers=3, random_state=42, cluster_std=1.5)

# Run Soft K-Means
K = 3
C, weights = soft_kmeans(X, K, beta=2.0)

# Plot results
plt.scatter(X[:, 0], X[:, 1], c=weights.argmax(axis=1), alpha=0.5, cmap='viridis')
plt.scatter(C[:, 0], C[:, 1], c='red', marker='x', s=200, label='Cluster Centers')
plt.legend()
plt.show()
