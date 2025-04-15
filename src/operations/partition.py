import numpy as np
import scipy
import scipy.linalg
import scipy.sparse
import scipy.sparse.linalg
from sklearn.cluster import KMeans
import src.util.matrix_util as mut
import src.util.graph_converter as graph_converter

def partition_graph(graph, num_groups):
    a_matrix, node_labels = graph_converter.graph_to_adjacency_matrix(graph)

    # Laplacian 
    affinity_matrix = mut.build_affinity_matrix(a_matrix)
    degree_matrix = mut.build_degree_matrix(affinity_matrix)
    d_i = scipy.linalg.fractional_matrix_power(degree_matrix, -0.5)
    laplacian = np.matmul(d_i, np.matmul(affinity_matrix, d_i))

    # Eigen data
    eigen_values, eigen_matrix = scipy.linalg.eigh(laplacian)

    row_num, col_num = eigen_matrix.shape

    sampled_eigen_matrix = mut.sample_range_of_columns(eigen_matrix, col_num - num_groups, col_num)

    # Clustering
    kmeans = KMeans(n_clusters=num_groups).fit(sampled_eigen_matrix)

    # Labeling
    group_mapping = {}
    for index, value in enumerate(node_labels):
        group_mapping[value] = str(kmeans.labels_[index])
    

    return group_mapping
