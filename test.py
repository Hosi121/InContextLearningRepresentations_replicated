import unittest
import networkx as nx
from graph import select_nodes

class TestSelectNodes(unittest.TestCase):

    def test_select_nodes_enough_concepts(self):
        graph = nx.cycle_graph(5)
        concepts = ["apple", "bird", "sand", "math", "tree"]
        node_concepts = select_nodes(graph, concepts)
        self.assertEqual(len(node_concepts), 5)

    def test_select_nodes_not_enough_concepts(self):
        graph = nx.cycle_graph(5)
        concepts = ["apple", "bird", "sand", "math"]
        with self.assertRaises(ValueError):
            select_nodes(graph, concepts)

if __name__ == '__main__':
    unittest.main()
