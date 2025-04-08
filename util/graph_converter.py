import numpy as np
from util.pydantic_models import Graph

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
    # Convert Pydantic Graph model to dictionary if needed
    if isinstance(graph, Graph):
        graph = {
            'nodes': {node_id: {'label': node.label} for node_id, node in graph.nodes.items()} if graph.nodes else {},
            'edges': [{'source': edge.source, 'target': edge.target, 'metadata': {'weight': edge.metadata.weight}} for edge in graph.edges],
            'directed': str(graph.directed).lower() if graph.directed is not None else 'false'
        }
    
    # Initialize empty adjacency list
    adj_list = {node_id: [] for node_id in graph['nodes'].keys()}
    
    # Process each edge
    for edge in graph['edges']:
        source = edge['source']
        target = edge['target']
        weight = edge['metadata'].get('weight', 1)  # Default weight is 1 if not specified
        
        # Add the edge to the adjacency list
        adj_list[source].append((target, weight))
        
        # If the graph is undirected, add the reverse edge
        if graph.get('directed', 'false').lower() == 'false':
            adj_list[target].append((source, weight))
    
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
    # Convert Pydantic Graph model to dictionary if needed
    if isinstance(graph, Graph):
        graph = {
            'nodes': {node_id: {'label': node.label} for node_id, node in graph.nodes.items()} if graph.nodes else {},
            'edges': [{'source': edge.source, 'target': edge.target, 'metadata': {'weight': edge.metadata.weight}} for edge in graph.edges],
            'directed': str(graph.directed).lower() if graph.directed is not None else 'false'
        }
    
    # Get ordered list of nodes and their labels
    node_order = list(graph['nodes'].keys())
    node_labels = [graph['nodes'][node_id]['label'] for node_id in node_order]
    n = len(node_order)
    
    # Create node to index mapping
    node_to_index = {node: idx for idx, node in enumerate(node_order)}
    
    # Initialize adjacency matrix with zeros
    adj_matrix = np.zeros((n, n))
    
    # Process each edge
    for edge in graph['edges']:
        source_idx = node_to_index[edge['source']]
        target_idx = node_to_index[edge['target']]
        weight = edge['metadata'].get('weight', 1)  # Default weight is 1 if not specified
        
        # Add the edge to the adjacency matrix
        adj_matrix[source_idx][target_idx] = weight
        
        # If the graph is undirected, add the reverse edge
        if graph.get('directed', 'false').lower() == 'false':
            adj_matrix[target_idx][source_idx] = weight
    
    return adj_matrix, node_labels 
