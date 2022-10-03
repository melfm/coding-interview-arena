
import numpy as np
# Inputs: X, mu, sigma


def gaussian(x_input, mu, sigma):

    variance = x_input - mu
    w_x = np.exp(1/ (2* sigma**2 )) * np.dot(np.transpose(variance),variance)

    return w_x


def calc_phi_elem(x_input, mu, A_matrix, phi_approx):

    # phi_i
    variance = x_input - mu
    phi = phi_approx + np.tranpose(variance) * np.tranpose(A_matrix)* A_matrix* (variance)

    return phi


def calc_phi(x_inputs, mus, sigma, A_matrix, phi_approx):

    # X_input = d-dim vector 
    # A_matrix = square_matrix d

    # check size of matrix A 


    total_sum_w = 0
    w_s = []
    for x_input in x_inputs:
        for mu in mus:
            w_i = gaussian(x_input, mu, sigma)
            total_sum_w += w_i
        w_s.append(total_sum_w)
        total_sum_w = 0


    w_phi_sum = 0

    for x_input in x_inputs:
        for mu in mus:
            w_i = gaussian(x_input, mu, sigma)
            phi_i = calc_phi_elem(x_input, mu, A_matrix, phi_approx)

            w_phi_dot_prod = np.dot(w_i, phi_i)

            w_phi_sum += w_phi_dot_prod


    phi_x = total_sum_w / w_phi_sum

    return phi_x


# D:2
# dim of input
D = 2
N = 3
input_x = [1, 2]

mus = []
sigmas = []
A_matrices = []

for n in range(N):
    mu_i = [0, 0]
    mus.append(mu_i)

    sigma = 1
    sigmas.append(sigma)

    A_matrix_i = [[1, 0], [0,1]]
    A_matrices.append(A_matrix_i)



