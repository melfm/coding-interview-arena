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
            check_neighbourhood(matrix[i][j], visit_map, matrix, i, j)
    return num_of_visited_countries


def map_matrix_island_string_version(row, col, input_string):
    """Similar idea to 'map_matrix_island_color', however in this case
    we are given the size of the grid, and an input string in the following
    format:
        Input: 6,4, '.....xx..x........x.....'
        Output: 2
    The task is to format this string into a matrix and count the number of
    x regions that are connected.
        ....
        .xx.
        .x..
        ....
        ..x.
        ....
    """
    string_list = list(input_string)

    # Break-up the string into chunks of size row and col
    chunks, chunk_size = len(string_list), col
    str_matrix = [
        string_list[i:i + chunk_size] for i in range(0, chunks, chunk_size)
    ]

    matrix = np.zeros((row, col))

    for i in range(0, row):
        for j in range(0, col):

            if str_matrix[i][j] == 'x':
                matrix[i][j] = -1

    # The rest of the code is as before
    visit_map = np.ones_like(matrix)
    num_of_visited_x = 0

    row_len = matrix.shape[0]
    col_len = matrix.shape[1]

    # Visit the cells
    for i in range(0, row_len):
        for j in range(0, col_len):
            if visit_map[i][j] == 0:
                continue
            # Only count X's
            if matrix[i][j] != 0:
                num_of_visited_x += 1
            check_neighbourhood(matrix[i][j], visit_map, matrix, i, j)
    return num_of_visited_x


def shorted_path_bin_maze(maze, start, end):
    """Shortest path in a Binary Maze.
    Given a MxN matrix where each element can either be 0 or 1.
    We need to find the shortest path between a given start
    cell to an end cell. The path can only be created out of a
    cell if its value is 1.

    Args:
        maze: A MxN matrix of binary values.
        start: An array in the form [i, j] of the starting location
            in the matrix.
        end: An array in the form [i, j] of the end location.
    """

    visit_map = np.zeros_like(maze)

    row_len = maze.shape[0]
    col_len = maze.shape[1]

    # Append distance info to the cell -> [i, j, distance]
    # starting with distance 0.
    start.append(0)
    queue = [start]
    visit_map[start[0], start[1]] = 1

    def is_valid(row, col, max_row, max_col):

        return (row >= 0) and (col >= 0) and \
            (row < (max_row - 1)) and (col < (max_col - 1))

    rowNum = [-1, 0, 0, 1]
    colNum = [0, -1, 1, 0]

    while queue:
        cell = queue.pop()
        current_distance = cell[2]

        if cell[0] == end[0] and cell[1] == end[1]:
            return cell[2]

        for i in range(4):
            # Check adjacent neighbours
            row = cell[0] + rowNum[i]
            col = cell[1] + colNum[i]
            if is_valid(row, col, row_len, col_len) and \
                    maze[row][col] and (not visit_map[row][col]):
                # Append distance information to the cell
                queue.append([row, col, current_distance + 1])
                visit_map[row][col] = 1

    # No path found!
    return -1


def set_matrix_row_col_all_zeros(matrix):
    """
    Write an algorithm such that if an element in an
    MxN matrix is 0, its entire row and column is set to 0
    """

    row_length = matrix.shape[0]
    col_length = matrix.shape[1]

    rows = np.zeros(row_length)
    cols = np.zeros(col_length)

    # Identify places with zeros first
    for i in range(row_length):
        for j in range(col_length):
            if matrix[i][j] == 0:
                rows[i] = 1
                cols[j] = 1

    for i in range(row_length):
        for j in range(col_length):
            if (rows[i] == 1 or cols[j] == 1):
                matrix[i][j] = 0

    return matrix


def isInvalidMatrixSpiral(matrix, r, c):
    mat_len = matrix.shape[0]
    if r < 0 or c < 0 or r >= mat_len or c >= mat_len or matrix[r][c] != 0:
        return True
    return False


def spiral(n):
    """
    Find the pattern and implement the function.
    input = 3
    1 2 3
    8 9 4
    7 6 5

    input = 4
    01 02 03 04
    12 13 14 05
    11 16 15 06
    10 09 08 07

    input = 8
    1 2 3 4 5 6 7 8
    28 29 30 31 32 33 34 9
    27 48 49 50 51 52 35 10
    26 47 60 61 62 53 36 11
    25 46 59 64 63 54 37 12
    24 45 58 57 56 55 38 13
    23 44 43 42 41 40 39 14
    22 21 20 19 18 17 16 15
    """

    dc = [1, 0, -1, 0]
    dr = [0, 1, 0, -1]
    matrix = np.zeros((n, n))

    dir = 0
    val = 1
    r = 0
    c = 0
    limit = n * n

    while (val <= limit):
        matrix[r][c] = val
        r += dr[dir]
        c += dc[dir]

        if (isInvalidMatrixSpiral(matrix, r, c)):
            r -= dr[dir]
            c -= dc[dir]
            dir = (dir + 1) % 4
            r += dr[dir]
            c += dc[dir]
        val += 1

    return matrix


def convolve2d_vanilla(matrix, kernel):
    """FB Coding question: Implement a convolution with a normal kernel.
    Then consider other types of convolution such as gaussian kernel and
    think about how to optimize the convolution operation.
    See: https://github.com/detkov/Convolution-From-Scratch/blob/main/convolution.py

    The kernel can be arbitrary or for Gaussian kernel or other options see:
    https://en.wikipedia.org/wiki/Kernel_(image_processing)

    This is a vanilla version which does not handle padding, varied stride, dilation.
    """

    n_row = matrix.shape[0]
    m_col = matrix.shape[1]

    k_row = kernel.shape[0]
    k_col = kernel.shape[1]

    out_row = n_row - 1
    out_col = m_col - 1

    matrix_out = np.zeros((out_row, out_col))

    slide_x_0 = 0
    slide_y_0 = 0

    for i in range(out_row):
        slide_x = slide_x_0 + i
        indices_x = [slide_x + l for l in range(k_row)]

        for j in range(out_col):
            slide_y = slide_y_0 + j
            indices_y = [slide_y + l for l in range(k_col)]
            submatrix = matrix[indices_x, :][:, indices_y]
            matrix_out[i][j] = np.sum(np.multiply(submatrix, kernel))

    return matrix_out

def _add_padding(matrix, padding):
    """ Pad the matrix so we can apply convolve2d.
    """

    n, m = matrix.shape
    r, c = padding[0], padding[1]

    padded_matrix = np.zeros((n + r*2, m + c*2))
    padded_matrix[r : n + r, c: m + c] = matrix
    return padded_matrix

def convolve2d(matrix, kernel, padding, stride, dilation):
    """ Apply convolution by considering padding, stride and dilation parameters.
    TODO: Figure out indices with dilation.
    """

    n_row = matrix.shape[0]
    m_col = matrix.shape[1]

    k_row = kernel.shape[0]
    k_col = kernel.shape[1]

    out_row = int((n_row + 2*padding[0] - k_row)/stride + 1)
    out_col = int((m_col + 2*padding[1] - k_col)/stride + 1)

    padded_mat = _add_padding(matrix, padding)

    matrix_out = np.zeros((out_row, out_col))

    slide_x_0 = 0
    slide_y_0 = 0

    for i in range(out_row):
        slide_x = slide_x_0 + i
        indices_x = [slide_x + l for l in range(k_row)]

        for j in range(out_col):
            slide_y = slide_y_0 + j
            indices_y = [slide_y + l for l in range(k_col)]
            submatrix = padded_mat[indices_x, :][:, indices_y]
            matrix_out[i][j] = np.sum(np.multiply(submatrix, kernel))

    return matrix_out
