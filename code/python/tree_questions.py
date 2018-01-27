"""Tree Questions."""


class TreeNode:
    """Binary Tree traversal.
    """

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
