
"""Multivariate Gaussian Probability Density Function."""
import numpy as np
import scipy.stats as sps


def my_logpdf(x, mu, covar):
  k = len(x)  # dimension
  a = np.transpose(x - mu)
  b = np.linalg.inv(covar)
  c = x - mu
  d = np.matmul(a, b)
  e = np.matmul(d, c)
  numer = np.exp(-0.5 * e)
  f = (2 * np.pi)**k
  g = np.linalg.det(covar)
  denom = np.sqrt(f * g)
  pdf = numer / denom
  return np.log(pdf)


# Sample inputs
# This is still 1D - can try with 2D input
mu = np.array([1.0, 3.0, 2.0], dtype=np.float32)
sigma = np.array([1.0, 1.0, 1.0], dtype=np.float32)
covar = np.diag(sigma)
x = np.array([1.5, 1.5, 1.5], dtype=np.float32)

print("\nu = ", end=""); print(mu)
print("\ncovar = ")
print(covar)
print("\nx = ", end=""); print(x)

logp1 = sps.multivariate_normal.logpdf(x, mu, covar)
print("\nlogpdf(x) using scipy logpdf() = %0.4f " % logp1)

logp2 = my_logpdf(x, mu, covar)
print("\nlogpdf(x) using my_logpdf()    = %0.4f " % logp2)