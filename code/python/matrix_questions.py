import numpy as np


def rotate_matrix(matrix):
    """Given an matrix represented by N x N matrix where each pixel in the
    matrix is 4 bytes write a method to rotate the matrix by 90 degrees
    """

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


def rotate_matrix_in_place(matrix, n):
    """Given an matrix represented by N x N matrix where each pixel in the
    matrix is 4 bytes write a method to rotate the matrix by 90 degrees
    Do this in place.
    """

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


def check_neighbourhood(colour, visit_map, matrix, i, j):

    row_len = matrix.shape[0]
    col_len = matrix.shape[1]

    if visit_map[i][j] == 0:
        return
    if matrix[i][j] != colour:
        return
    visit_map[i][j] = 0

    if i < row_len - 1:
        check_neighbourhood(colour, visit_map, matrix, i + 1, j)
    if i != 0:
        check_neighbourhood(colour, visit_map, matrix, i - 1, j)

    if j < col_len - 1:
        check_neighbourhood(colour, visit_map, matrix, i, j + 1)

    if j != 0:
        check_neighbourhood(colour, visit_map, matrix, i, j - 1)


def map_matrix_island_color_recursive(matrix):
    """A rectangular N x M map contains colored areas. The areas
    in the map belong to the same country if:
        - They have the same color
        - It is possible to travel from one area to the other
        orthogonally (that is by moving only north, south, west or
        east.
    The map is a represented by a matrix and colours by the element
    of the matrix.
    Write a function to return number of different countries.
    Complexity -> Expected worst-case time and space of O(N*M).
    """

    visit_map = np.ones_like(matrix)
    num_of_visited_countries = 0

    row_len = matrix.shape[0]
    col_len = matrix.shape[1]

    # Visit the cells
    for i in range(0, row_len):
        for j in range(0, col_len):
            if visit_map[i][j] == 0:
                continue
            num_of_visited_countries += 1
            check_neighbourhood(matrix[i][j],
                                visit_map,
                                matrix,
                                i, j)
    return num_of_visited_countries
