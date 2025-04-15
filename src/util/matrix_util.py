import numpy as np
import math 
import copy

def build_affinity_matrix(adjacency_matrix, sigma=1):
    shape = adjacency_matrix.shape
    num_rows, num_cols = shape

    max_abs_value = max(adjacency_matrix.max(), abs(adjacency_matrix.min()))

    output = np.ones(shape)
    for row_index in range(num_rows):
        for col_index in range(num_cols):
            if col_index != row_index:
                output[row_index][col_index] = 1 - (adjacency_matrix[row_index][col_index] / max_abs_value)

    for row_index in range(num_rows):
        for col_index in range(num_cols):
            if col_index != row_index:
                output[row_index][col_index] = math.exp(-0.5 * (output[row_index][col_index]**2) / sigma ** 2)
            else:
                output[row_index][col_index] = 0

    return output

def build_degree_matrix(input_matrix):
    shape = input_matrix.shape
    num_rows, num_cols = shape

    if num_rows != num_cols:
        raise Exception("-- Input matrix must be square --")

    row_tallys = []
    for i in range(num_rows):
        tally = 0
        for j in range(num_cols):
            tally += input_matrix[i, j]
        row_tallys.append(tally)

    output = np.zeros(shape)
    for i in range(num_rows):
        output[i][i] = row_tallys[i]

    return output

# Start and end inclusive [start, end] (zero indexed)
def sample_range_of_columns(matrix, start, end):
    return matrix[:,start:end + 1]


def normalized_matrix_rows(matrix_input):
    matrix = np.zeros(matrix_input.shape)
    
    for y, row in enumerate(matrix_input):
        length = np.linalg.norm(row)
        for x, item in enumerate(row):
            matrix[y][x] = item / length

    return matrix

def normalize_matrix_by_longest_row(matrix):
    row_norms = np.linalg.norm(matrix, axis=1)
    max_norm = np.max(row_norms)

    if max_norm == 0:
        return matrix
    
    normalized_matrix = matrix / max_norm
    
    return normalized_matrix
