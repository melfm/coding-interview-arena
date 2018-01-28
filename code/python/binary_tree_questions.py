"""Binary Tree Questions."""


class TreeNode:

    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value

    def insert_right(self, node, value):
        if node.right is None:
            self.right = TreeNode(value)

        else:
            new_node = TreeNode(value)
            new_node.left = self.left
            new_node.right = node

    def insert_left(self, node, value):
        if node.left is None:
            self.left = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.left = None
            new_node.right = None

    def traverse_inorder(self, node, children_list=[]):
        # In-Order: Traverse left node, current node, then right

        if node is None:
            return children_list

        self.traverse_inorder(node.left, children_list)
        children_list.append(node.value)
        self.traverse_inorder(node.right, children_list)

    def traverse_preorder(self, node, children_list=[]):
        # Pre-Order: Traverse current node, then left node,
        # then right node

        if node is None:
            return children_list

        children_list.append(node.value)
        self.traverse_preorder(node.left, children_list)
        self.traverse_preorder(node.right, children_list)

    def traverse_postorder(self, node, children_list=[]):
        # Post-Order: Traverse left node, then right node,
        # then current node.

        if node is None:
            return children_list

        self.traverse_postorder(node.left, children_list)
        self.traverse_postorder(node.right, children_list)
        children_list.append(node.value)

    def max_depth(self, node):
        # Find the max depth of a binary tree
        if node is None:
            return 0

        return 1 + max(self.max_depth(node.right),
                       self.max_depth(node.left))

    def min_depth(self, node):
        # Find the min depth of a binary tree
        if node is None:
            return 0

        return 1 + min(self.min_depth(node.right),
                       self.min_depth(node.left))

    def is_tree_balanced(self, node):
        # Find whether a binary tree is balanced or not

        if node is None:
            return True

        height_diff = self.max_depth(node.left) - self.max_depth(node.right)

        if abs(height_diff) > 1:
            return False
        else:
            return self.is_tree_balanced(node.left) and\
                self.is_tree_balanced(node.right)
