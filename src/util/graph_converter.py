import numpy as np
from src.util.pydantic_models import Graph

def _convert_graph_to_dict(graph):
    """Helper function to convert Pydantic Graph to dictionary format."""
    if isinstance(graph, Graph):
        return {
            'nodes': {node_id: {'label': node.label} for node_id, node in graph.nodes.items()} if graph.nodes else {},
            'edges': [{'source': edge.source, 'target': edge.target, 'metadata': {'weight': edge.metadata.weight}} for edge in graph.edges],
            'directed': str(graph.directed).lower() if graph.directed is not None else 'false'
        }
    return graph

def _process_edge(edge, graph, adj_list):
    """Helper function to process a single edge."""
    source, target = edge['source'], edge['target']
    weight = edge['metadata'].get('weight', 1)
    
    adj_list[source].append((target, weight))
    if graph.get('directed', 'false').lower() == 'false':
        adj_list[target].append((source, weight))

def graph_to_adjacency_list(graph):
    """
    Convert a graph object to an adjacency list representation.
    
    Args:
        graph (dict or Graph): A graph object containing:
            - nodes: Dictionary of nodes with their labels
            - edges: List of edges with source, target, and metadata
            - directed: Boolean indicating if the graph is directed
    
    Returns:
        dict: Adjacency list representation where keys are node IDs and values are lists of tuples
              containing (neighbor_id, weight) pairs
    """
    graph = _convert_graph_to_dict(graph)
    adj_list = {node_id: [] for node_id in graph['nodes'].keys()}
    
    for edge in graph['edges']:
        _process_edge(edge, graph, adj_list)
    
    return adj_list

def graph_to_adjacency_matrix(graph):
    """
    Convert a graph object to an adjacency matrix representation.
    
    Args:
        graph (dict or Graph): A graph object containing:
            - nodes: Dictionary of nodes with their labels
            - edges: List of edges with source, target, and metadata
            - directed: Boolean indicating if the graph is directed
    
    Returns:
        tuple: (adjacency_matrix, node_labels) where:
            - adjacency_matrix: 2D numpy array where matrix[i][j] is the weight of edge from node i to node j
            - node_labels: List of node labels in the order they appear in the matrix
    """
    graph = _convert_graph_to_dict(graph)
    node_order = list(graph['nodes'].keys())
    node_labels = [graph['nodes'][node_id]['label'] for node_id in node_order]
    n = len(node_order)
    
    adj_matrix = np.zeros((n, n))
    node_to_index = {node: idx for idx, node in enumerate(node_order)}
    
    for edge in graph['edges']:
        source_idx = node_to_index[edge['source']]
        target_idx = node_to_index[edge['target']]
        weight = edge['metadata'].get('weight', 1)
        
        adj_matrix[source_idx][target_idx] = weight
        if graph.get('directed', 'false').lower() == 'false':
            adj_matrix[target_idx][source_idx] = weight
    
    return adj_matrix, node_labels 
