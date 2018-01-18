import numpy as np

import pdb


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


def map_matrix_island_color(matrix):
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

            current_cell = matrix[i][j]
            print('current i and j ->', i, ',', j)

            print(visit_map)
            if visit_map[i][j] == 1:
                print('Incrementing for ',  i, ',', j)

                num_of_visited_countries += 1
                visit_map[i][j] = 0

            # Check neighbors
            # Check left
            if j < col_len - 1:
                if current_cell == matrix[i][j+1]:
                    visit_map[i][j+1] = 0
            if j != 0:
                # Check Right
                if current_cell == matrix[i][j-1]:
                    visit_map[i][j-1] = 0

            # Check top
            if i != 0:
                if current_cell == matrix[i-1][j]:
                    visit_map[i-1][j] = 0

            if i < row_len - 1:
                # Check bottom
                if current_cell == matrix[i+1][j]:
                    visit_map[i+1][j] = 0

    print('Map', visit_map)
    print('Num ', num_of_visited_countries)
    return num_of_visited_countries
