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
            print('Breadth First Search -> ', nodes)

        nodes = graph.bfs(self.graph_two, 'A')
        exp_nodes = ['A', 'B', 'C', 'D', 'E', 'F']

        self.assertEqual(nodes, exp_nodes)

        if self.dump_output:
            print('Breadth First Search  -> ', nodes)

    def test_dfs(self):

        nodes = graph.dfs(self.graph_one, 'A')
        exp_nodes = ['A', 'E', 'D', 'B', 'C', 'G', 'F']
        self.assertEqual(nodes, exp_nodes)

        if self.dump_output:
            print('Depth First Search -> ', nodes)

        nodes = graph.dfs(self.graph_two, 'A')
        exp_nodes = ['A', 'C', 'F', 'E', 'B', 'D']
        self.assertEqual(nodes, exp_nodes)

        if self.dump_output:
            print('Depth First Search -> ', nodes)

    def test_dfs_recursive(self):

        nodes = []
        graph.dfs_recursive(self.graph_one, 'A', nodes)
        exp_nodes = ['A', 'B', 'D', 'E', 'C', 'F', 'G']
        self.assertEqual(nodes, exp_nodes)

        if self.dump_output:
            print('Depth First Search -> ', nodes)

    def test_path_exist(self):

        graph_data = {1: [2, 3],
                      2: [4, 5, 6],
                      3: [7, 8, 9],
                      8: [10]}

        path_found = graph.path_exist(graph_data, 1, 1, 6)
        if self.dump_output:
            print('Path found.')
        self.assertTrue(path_found[0])

        path_found = graph.path_exist(
            graph_data, 1, 3, 4, [], False, [])
        self.assertFalse(path_found)


if __name__ == '__main__':
    unittest.main()
