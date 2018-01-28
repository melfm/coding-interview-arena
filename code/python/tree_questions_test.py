import unittest

import tree_questions as trees


class TreeQuestionTest(unittest.TestCase):

    dump_output = True

    def test_tree_traversal(self):
        root_node = trees.TreeNode(1)

        root_node.add_children([4, 3])

        root_node.children.add_child(2)

        root_node.children.add_child(5)
        root_node.children.next.add_child(8)

        exp_all_children = [1, 4, 3, 2, 5, 8]

        all_children = []
        root_node.traverse_tree(root_node,
                                all_children)

        self.assertEqual(all_children,
                         exp_all_children)
        if self.dump_output:
            print(all_children)


if __name__ == '__main__':
    unittest.main()
