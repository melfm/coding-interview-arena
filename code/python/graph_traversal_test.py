import unittest

import graph_traversal_questions as graph


class GraphTraversalQuestionsTest(unittest.TestCase):

    dump_output = True

    @classmethod
    def setUpClass(cls):
        cls.graph_one = {'A': ['B', 'C', 'E'],
                         'B': ['A', 'D', 'E'],
                         'C': ['A', 'F', 'G'],
                         'D': ['B'],
                         'E': ['A', 'B', 'D'],
                         'F': ['C'],
                         'G': ['C']}

        cls.graph_two = {'A': ['B', 'C'],
                         'B': ['A', 'D', 'E'],
                         'C': ['A', 'F'],
                         'D': ['B'],
                         'E': ['B', 'F'],
                         'F': ['C', 'E']}

    def test_bfs(self):

        nodes = graph.bfs(self.graph_one, 'A')
        exp_nodes = ['A', 'B', 'C', 'E', 'D', 'F', 'G']

        self.assertEqual(nodes, exp_nodes)

        if self.dump_output:
            print('BFS -> ', nodes)

        nodes = graph.bfs(self.graph_two, 'A')
        exp_nodes = ['A', 'B', 'C', 'D', 'E', 'F']

        self.assertEqual(nodes, exp_nodes)

        if self.dump_output:
            print('BFS -> ', nodes)

    def test_dfs(self):

        nodes = graph.dfs(self.graph_one, 'A')
        exp_nodes = ['A', 'E', 'D', 'B', 'C', 'G', 'F']
        self.assertEqual(nodes, exp_nodes)

        if self.dump_output:
            print('DFS -> ', nodes)

        nodes = graph.dfs(self.graph_two, 'A')
        exp_nodes = ['A', 'C', 'F', 'E', 'B', 'D']
        self.assertEqual(nodes, exp_nodes)

        if self.dump_output:
            print('DFS -> ', nodes)


if __name__ == '__main__':
    unittest.main()
