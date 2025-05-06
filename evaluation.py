import torch

def prepare_model_input(walk, node_concepts, tokenizer, context_size):
    text = " ".join([node_concepts[node] for node in walk])
    text = text[:context_size]
    inputs = tokenizer(text, return_tensors="pt")
    return inputs

def evaluate_model(model, inputs):
    with torch.no_grad():
        outputs = model(**inputs, output_hidden_states=True)
    return outputs.logits, outputs.hidden_states

import networkx as nx

def calculate_dirichlet_energy(hidden_states, graph, layer=-1):
    if layer == -1:
        layer = len(hidden_states) - 1

    activations = hidden_states[layer].squeeze()
    dirichlet_energy = 0.0
    adjacency_matrix = nx.adjacency_matrix(graph).toarray()
    num_nodes = adjacency_matrix.shape[0]

    for i in range(num_nodes):
        for j in range(num_nodes):
            if adjacency_matrix[i, j] == 1:
                h_i = activations[i]
                h_j = activations[j]
                dirichlet_energy += torch.sum((h_i - h_j) ** 2)

    dirichlet_energy = 0.5 * dirichlet_energy
    return dirichlet_energy

def calculate_accuracy(logits, walk, tokenizer):
    predicted_token_id = torch.argmax(logits[-1, :]).item()
    predicted_token = tokenizer.decode(predicted_token_id)
    actual_token = " ".join([node for node in walk[1:]]) # walk[0] is the start node
    
    if len(actual_token.split()) > 0:
      actual_token = actual_token.split()[0]
    else:
      return 0.0

    if predicted_token == actual_token:
        return 1.0
    else:
        return 0.0
