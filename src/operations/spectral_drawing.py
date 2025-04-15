import numpy as np
import scipy
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import src.util.matrix_util as mut
import src.util.graph_converter as graph_converter

def spectral_drawing(edges, num_dimensions):
    a_matrix, node_labels = graph_converter.graph_to_adjacency_matrix(edges)

    eigen_values, eigen_matrix = np.linalg.eigh(a_matrix)
    _row_num, col_num = eigen_matrix.shape

    num_dimensions = min(num_dimensions, col_num)

    pca = PCA(n_components=num_dimensions)
    pca_transformed = pca.fit_transform(eigen_matrix)

    normalized_output = mut.normalize_matrix_by_longest_row(pca_transformed)

    output = {}

    for i, row in enumerate(normalized_output):
        output[node_labels[i]] = list(row)

    return output
