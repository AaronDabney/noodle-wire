import numpy as np
import scipy
from sklearn.cluster import KMeans
import util.matrix_util as mut
import util.graph_converter as graph_converter

def spectral_drawing(edges, num_dimensions):
    a_matrix, node_labels = graph_converter.graph_to_adjacency_matrix(edges)

    eigen_values, eigen_matrix = np.linalg.eigh(a_matrix)

    _row_num, col_num = eigen_matrix.shape

    num_dimensions = min(num_dimensions, col_num)

    sampled_eigen_matrix = mut.sample_range_of_columns(eigen_matrix, 1, num_dimensions)

    output = {}

    for i, row in enumerate(sampled_eigen_matrix):
        output[node_labels[i]] = list(row)

    return output
