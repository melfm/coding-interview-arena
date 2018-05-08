import numpy as np
import unittest

import binary_tree_questions as trees


class BinaryTreeQuestionTest(unittest.TestCase):

    dump_output = False

    @classmethod
    def setUpClass(cls):
        cls.root = trees.TreeNode(1)

        cls.root.left = trees.TreeNode(2)
        cls.root.right = trees.TreeNode(3)

        cls.root.left.left = trees.TreeNode(4)
        cls.root.left.right = trees.TreeNode(5)
        cls.root.right.left = trees.TreeNode(6)
        cls.root.right.right = trees.TreeNode(7)

    def test_in_order_traversal(self):

        all_children = []
        self.root.traverse_inorder(self.root,
                                   all_children)

        exp_child_values = [4, 2, 5, 1, 6, 3, 7]

        self.assertEqual(all_children,
                         exp_child_values)

        if self.dump_output:
            print(all_children)

    def test_pre_order_traversal(self):

        all_children = []
        self.root.traverse_preorder(self.root,
                                    all_children)

        exp_child_values = [1, 2, 4, 5, 3, 6, 7]

        self.assertEqual(all_children,
                         exp_child_values)

        if self.dump_output:
            print(all_children)

    def test_post_order_traversal(self):

        all_children = []
        self.root.traverse_postorder(self.root,
                                     all_children)

        exp_child_values = [4, 5, 2, 6, 7, 3, 1]

        self.assertEqual(all_children,
                         exp_child_values)

        if self.dump_output:
            print(all_children)

    def test_find_max_depth(self):
        root = trees.TreeNode(1)

        root.left = trees.TreeNode(2)
        root.right = trees.TreeNode(3)

        root.left.left = trees.TreeNode(4)
        root.left.right = trees.TreeNode(5)
        root.right.left = trees.TreeNode(6)
        root.right.right = trees.TreeNode(7)

        root.right.right.left = trees.TreeNode(9)
        root.right.right.right = trees.TreeNode(8)
        root.right.right.left.right = trees.TreeNode(10)

        tree_depth = root.max_depth(root)

        self.assertEqual(tree_depth, 5)

    def test_find_min_depth(self):
        root = trees.TreeNode(1)

        root.left = trees.TreeNode(2)
        root.right = trees.TreeNode(3)

        root.left.left = trees.TreeNode(4)
        root.left.right = trees.TreeNode(5)
        root.right.left = trees.TreeNode(6)
        root.right.right = trees.TreeNode(7)

        root.right.right.left = trees.TreeNode(9)
        root.right.right.right = trees.TreeNode(8)
        root.right.right.left.right = trees.TreeNode(10)

        tree_depth = root.min_depth(root)

        self.assertEqual(tree_depth, 3)

    def test_is_tree_balanced(self):
        root = trees.TreeNode(1)

        root.left = trees.TreeNode(2)
        root.right = trees.TreeNode(3)

        root.left.left = trees.TreeNode(4)
        root.left.right = trees.TreeNode(5)
        root.right.left = trees.TreeNode(6)
        root.right.right = trees.TreeNode(7)

        is_balanced = root.is_tree_balanced(root)
        self.assertEqual(is_balanced, True)

        root.right.right.left = trees.TreeNode(9)
        root.right.right.right = trees.TreeNode(8)
        root.right.right.left.right = trees.TreeNode(10)
        is_balanced = root.is_tree_balanced(root)
        self.assertEqual(is_balanced, False)

    def test_create_tree_from_sorted_array(self):

        array = [0, 1, 2, 3, 4, 5, 6]

        tree_var = trees.create_tree_from_sorted_array(array)

        all_nodes = []
        exp_nodes = [0, 1, 2, 3, 4, 5, 6]
        tree_var.traverse_inorder(tree_var, all_nodes)
        np.testing.assert_array_equal(all_nodes, exp_nodes)

        all_nodes = []
        exp_nodes = [3, 1, 5, 0, 2, 4, 6]
        tree_var.traverse_bfs(tree_var, all_nodes)
        np.testing.assert_array_equal(all_nodes, exp_nodes)

    def test_find_first_common_ancestor(self):

        array = [1, 2, 3, 4, 5, 6, 7, 8]

        tree_var = trees.create_tree_from_sorted_array(array)

        all_nodes = []
        tree_var.traverse_bfs(tree_var, all_nodes)

        node_a = tree_var.right.right.right
        node_b = tree_var.right.left
        common_ancestor = trees.find_first_common_ancestor(tree_var,
                                                           node_a,
                                                           node_b)
        self.assertEqual(common_ancestor.value, 6)


if __name__ == '__main__':
    unittest.main()
