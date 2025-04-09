import numpy as np
from src.util.pydantic_models import Graph


def graph_to_adjacency_list(graph):
    adj_list = {node_id: [] for node_id in graph.nodes.keys()}
    
    for edge in graph.edges:
        source, target = edge.source, edge.target
        weight = edge.metadata.weight
        adj_list[source].append((target, weight))

        if not graph.directed:
            adj_list[target].append((source, weight))

    return adj_list

def graph_to_adjacency_matrix(graph):
    node_order = list(graph.nodes.keys())
    node_labels = [node.label for node in graph.nodes.values()]
    num_nodes = len(node_order)
    
    adj_matrix = np.zeros((num_nodes, num_nodes))
    node_to_index = {node: idx for idx, node in enumerate(node_order)}
    
    for edge in graph.edges:
        source_idx = node_to_index[edge.source]
        target_idx = node_to_index[edge.target]
        weight = edge.metadata.weight
        
        adj_matrix[source_idx][target_idx] = weight
        if not graph.directed:
            adj_matrix[target_idx][source_idx] = weight
    
    return adj_matrix, node_labels 
