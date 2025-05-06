import numpy as np
import os
import datetime
from model import load_model
from save_experiment_data import save_experiment_data
from graph import create_graph, select_nodes
from walk import generate_random_walk
from evaluation import prepare_model_input, evaluate_model, calculate_dirichlet_energy, calculate_accuracy
#from analysis import analyze_results

def run_experiment(graph_type="grid", graph_size=(4, 4), num_nodes=10, concepts=["apple", "bird", "sand", "math"], semantic_correlation="random", walk_steps=10, context_size=50):
    # 日付を取得
    date = datetime.date.today().strftime("%Y%m%d")

    # ディレクトリ名を作成
    result_dir = f"result_{date}"

    experiment_settings = {
        "graph_type": graph_type,
        "graph_size": graph_size,
        "num_nodes": num_nodes,
        "concepts": concepts,
        "semantic_correlation": semantic_correlation,
        "walk_steps": walk_steps,
        "context_size": context_size
    }

    model, tokenizer = load_model()
    graph = create_graph(graph_type, graph_size, num_nodes)
    start_node = np.random.choice(list(graph.nodes))
    node_concepts = select_nodes(graph, concepts, semantic_correlation)
    walk = generate_random_walk(graph, start_node, walk_steps)
    inputs = prepare_model_input(walk, node_concepts, tokenizer, context_size)
    logits, hidden_states = evaluate_model(model, inputs)

    save_experiment_data(result_dir, experiment_settings, hidden_states)

    dirichlet_energy = calculate_dirichlet_energy(hidden_states, graph)
    accuracy = calculate_accuracy(logits, walk, tokenizer)
    #analyze_results(outputs, graph, walk)
    return logits, dirichlet_energy, accuracy

if __name__ == "__main__":
    logits, dirichlet_energy, accuracy = run_experiment()
    print("Logits:", logits)
    print("Dirichlet Energy:", dirichlet_energy)
    print("Accuracy:", accuracy)
