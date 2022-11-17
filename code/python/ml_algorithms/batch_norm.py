
""" Implement batch-norm using numpy.
The code is non-runnable - just the algorithmic idea.
See :
1) https://melfm.github.io/posts/2018-08-Understanding-Normalization/
2) https://kevinzakka.github.io/2016/09/14/batch_normalization/
3) https://kratzert.github.io/2016/02/12/understanding-the-gradient-flow-through-the-batch-normalization-layer.html
"""

import numpy as np


def batchnorm_forward(x, gamma, beta, eps=1e-5):
    N, D = x.shape
    
    sample_mean = x.mean(axis=0)
    sample_var = x.var(axis=0)
    
    std = np.sqrt(sample_var + eps)
    x_centered = x - sample_mean
    x_norm = x_centered / std
    out = gamma * x_norm + beta
    
    cache = (x_norm, x_centered, std, gamma)

    return out, cache

def batchnorm_backward(dout, cache):
    N = dout.shape[0]
    x_norm, x_centered, std, gamma = cache
    dgamma = (dout * x_norm).sum(axis=0)
    dbeta = dout.sum(axis=0)
    
    dx_norm = dout * gamma
    dx_centered = dx_norm / std
    dmean = -(dx_centered.sum(axis=0) + 2/N * x_centered.sum(axis=0))
    dstd = (dx_norm * x_centered * -std**(-2)).sum(axis=0)
    dvar = dstd / 2 / std
    dx = dx_centered + (dmean + dvar * 2 * x_centered) / N

    return dx, dgamma, dbeta