import unittest

import binary_tree_questions as trees


class BinaryTreeQuestionTest(unittest.TestCase):

    dump_output = True

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


if __name__ == '__main__':
    unittest.main()
