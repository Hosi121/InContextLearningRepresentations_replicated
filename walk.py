import numpy as np

def generate_random_walk(graph, start_node, steps):
    walk = [start_node]
    current_node = start_node
    for _ in range(steps):
        neighbors = list(graph.neighbors(current_node))
        if not neighbors:
            break
        next_node = np.random.choice(neighbors)
        walk.append(next_node)
        current_node = next_node
    return walk
