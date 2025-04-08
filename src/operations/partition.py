import numpy as np
import scipy
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
    eigen_data = np.linalg.eigh(laplacian)
    ortho_eigen_matrix = mut.build_orthogonal_eigen_matrix(eigen_data)
    row_num, col_num = ortho_eigen_matrix.shape

    sampled_eigen_matrix = mut.sample_range_of_columns(ortho_eigen_matrix, col_num - num_groups, col_num)
    normalized_eigen_matrix = mut.normalized_matrix_rows(sampled_eigen_matrix)

    # Clustering
    kmeans = KMeans(n_clusters=num_groups).fit(normalized_eigen_matrix)

    # Labeling
    group_mapping = {}
    for index, value in enumerate(node_labels):
        group_mapping[value] = str(kmeans.labels_[index])
    

    return group_mapping
