import unittest

import tree_questions as trees


class TreeQuestionTest(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
