import numpy as np


def isPowerOf3_loop(n):

    if n < 1:
        return False

    while(n % 3 == 0):
        n /= 3

    return n == 1


def isPowerOf3_int_limit(n):
    return n > 0 and 1162261467 % n == 0


def isPowerOf3_recursive(n):

    if n < 1:
        return False

    if n == 1:
        return True

    return isPowerOf3_recursive(n/3)


# Given an matrix represented by N x M matrix where each pixel in the
# matrix is 4 bytes write a method to rotate the matrix by 90 degrees
def rotate_matrix(matrix):

    row = matrix.shape[0]
    col = matrix.shape[1]

    new_matrix = np.zeros((col, row))

    outer_row = new_matrix.shape[1] - 1

    for i in range(matrix.shape[0]):
        # copy the first row
        current_row = matrix[i, :]
        new_matrix[:, outer_row] = current_row

        outer_row -= 1

    return new_matrix

# Given an matrix represented by N x N matrix where each pixel in the
# matrix is 4 bytes write a method to rotate the matrix by 90 degrees
# Do this in place


def rotate_matrix_in_place(matrix, n):

    for layer in range(n):

        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            # offset gets reduced for inner matrix
            offset = i - first
            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last - offset][first]
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top

    return matrix
