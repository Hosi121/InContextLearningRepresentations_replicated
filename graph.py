import networkx as nx
import numpy as np

def create_graph(graph_type="grid", size=(4, 4), num_nodes=10):
    if graph_type == "grid":
        graph = nx.grid_2d_graph(size[0], size[1])
    elif graph_type == "ring":
        graph = nx.cycle_graph(num_nodes)
    elif graph_type == "hexagonal":
        graph = nx.hexagonal_lattice_graph(size[0], size[1])
    else:
        raise ValueError("Invalid graph type")
    return graph

def select_nodes(graph, concepts, semantic_correlation="random"):
    if len(concepts) < len(graph.nodes):
        raise ValueError("Not enough concepts for the graph")

    node_concepts = {}
    nodes = list(graph.nodes)
    np.random.shuffle(nodes)

    if semantic_correlation == "random":
        np.random.shuffle(concepts)
        for i, node in enumerate(nodes):
            node_concepts[node] = concepts[i]
    elif semantic_correlation == "correlated":
        # 意味的に相関のある概念を選択するロジックを実装
        pass
    else:
        raise ValueError("Invalid semantic correlation type")
    return node_concepts
