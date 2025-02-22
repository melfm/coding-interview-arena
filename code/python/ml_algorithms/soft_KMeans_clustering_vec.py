import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

def soft_kmeans(X, K, beta=1.0, max_iters=100, tol=1e-4):
    """Soft K-Means Clustering Implementation"""
    N, D = X.shape
    
    # Initialize cluster centers randomly
    C = X[np.random.choice(N, K, replace=False)]
    
    for _ in range(max_iters):
        # Compute responsibilities (soft assignments)
        distances = np.linalg.norm(X[:, np.newaxis] - C, axis=2)**2
        weights = np.exp(-beta * distances)
        weights /= weights.sum(axis=1, keepdims=True)
        
        # Update cluster centers
        new_C = (weights.T @ X) / weights.sum(axis=0)[:, None]
        
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
