"""Binary Tree Questions."""

from collections import deque
from typing import List, Optional


class TreeNode:

    def __init__(self, value):
        # This is buggy TODO fix.

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

    def traverse_bfs(self, node, children_list=[]):
        # Breadth-first search for binary tree

        if node is None:
            return

        queue = []
        queue.append(node)

        while len(queue) > 0:
            curr_node = queue.pop(0)
            children_list.append(curr_node.value)

            if curr_node.left is not None:
                queue.append(curr_node.left)
            if curr_node.right is not None:
                queue.append(curr_node.right)

    def max_depth(self, node):
        # Find the max depth of a binary tree
        if node is None:
            return 0

        return 1 + max(self.max_depth(node.right), self.max_depth(node.left))

    def min_depth(self, node):
        # Find the min depth of a binary tree
        if node is None:
            return 0

        return 1 + min(self.min_depth(node.right), self.min_depth(node.left))

    def is_tree_balanced(self, node):
        # Find whether a binary tree is balanced or not

        if node is None:
            return True

        height_diff = self.max_depth(node.left) - self.max_depth(node.right)

        if abs(height_diff) > 1:
            return False
        else:
            return self.is_tree_balanced(node.left) and self.is_tree_balanced(
                node.right
            )

    def is_tree_BST(self, node):
        """Check if a binary tree is BST or not. A BST satisfies the following
        conditions:
        • Left subtree contains only nodes with keys less than node.
        • Right subtree contains only nodes with keys greater than node.
        • Both the left and right subtrees must also be binary search trees.

        The following code traverses the tree while keeping track of min and max
        on each branch. Consider what happens in the following tree:
                                    3
                                  /   \
                                 2     5
                                / \
                               1   4
        We call the following recursive functions :
            node(3, MIN, MAX)
                node(2, MIN, 3)
                    node(1, MIN, 2)
                    node(4, 2, 3)  -----> Note the condition is broken here.
                node(5, 3, MAX)

        """
        import sys

        min_val = -sys.maxsize - 1
        max_val = sys.maxsize

        def is_valid_BST(node, min_val, max_val):

            if node is None:
                return True

            return (
                node.value > min_val
                and node.value < max_val
                and is_valid_BST(node.left, min_val, node.value)
                and is_valid_BST(node.right, node.value, max_val)
            )

        return is_valid_BST(node, min_val, max_val)

    def insert(self, node, new_value):
        # This is typically a binary search tree insertion
        # Since we check the left and right children values
        # but remember its not a balanced tree, or a heap
        # so no node replacing is happening

        # Check left
        if new_value > node.value:
            # if it has no right node
            if node.right is None:
                new_node = TreeNode(new_value)
                node.right = new_node
            else:
                self.insert(node.right, new_value)

        elif new_value < node.value:
            # if it has no left node
            if node.left is None:
                new_node = TreeNode(new_value)
                node.left = new_node
            else:
                self.insert(node.left, new_value)


def create_tree_from_sorted_array(array):
    """Q: Given a sorted (increasing order) array, write an algorithm to
    create a binary tree with minimal height.
    """

    def add_to_tree(array, start, end):

        if end < start:
            return

        middle = int((start + end) / 2)
        node = TreeNode(array[middle])
        node.left = add_to_tree(array, start, middle - 1)
        node.right = add_to_tree(array, middle + 1, end)
        return node

    return add_to_tree(array, 0, len(array) - 1)


def find_first_common_ancestor(tree, node_a, node_b):
    """Design an algorithm to find the first common ancestor of two nodes
    in a binary tree. Avoid storing additional nodes in a data structure.
    NOTE: This is not necessarily a binary *search* tree.
    """

    def covers(tree, node):

        if tree is None:
            return False

        if tree == node:
            return True

        return covers(tree.left, node) or covers(tree.right, node)

    if covers(tree.left, node_a) and covers(tree.left, node_b):
        return find_first_common_ancestor(tree.left, node_a, node_b)

    if covers(tree.right, node_a) and covers(tree.right, node_b):
        return find_first_common_ancestor(tree.right, node_a, node_b)

    return tree


#######################
TWO_NODES_FOUND = 2
ONE_NODE_FOUND = 1
NO_NODE_FOUND = 0
#######################


def find_first_common_ancestor_v2(root, node_a, node_b):
    """For any node r we know the following:
    - If node_a is on one side and node_b is on the other side, r is
    the first common ancestor.
    - Otherwise the first common ancestor is either on the left or right.
    """

    def covers(root, node_a, node_b):
        res = NO_NODE_FOUND
        if root is None:
            return res
        if root == node_a or root == node_b:
            res += 1
        res += covers(root.left, node_a, node_b)
        if res == TWO_NODES_FOUND:
            return res
        res += covers(root.right, node_a, node_b)
        return res

    if node_a == node_b and (root.left == node_a or root.right == node_a):
        return root

    #################
    # Check left side
    #################
    nodes_from_left = covers(root.left, node_a, node_b)

    if nodes_from_left == TWO_NODES_FOUND:
        if root.left == node_a or root.left == node_b:
            return root.left
        else:
            return find_first_common_ancestor_v2(root.left, node_a, node_b)
    elif nodes_from_left == ONE_NODE_FOUND:
        if root == node_a:
            return node_a
        elif root == node_b:
            return node_b

    ##################
    # Check right side
    ##################
    nodes_from_right = covers(root.right, node_a, node_b)

    if nodes_from_right == TWO_NODES_FOUND:
        if root.right == node_a or root.right == node_b:
            return root.right
        else:
            return find_first_common_ancestor_v2(root.right, node_a, node_b)

    elif nodes_from_right == ONE_NODE_FOUND:
        if root == node_a:
            return node_a
        elif root == node_b:
            return node_b

    # The nodes are on each side, so the only common ancestor is the root
    if nodes_from_left == ONE_NODE_FOUND and nodes_from_right == ONE_NODE_FOUND:
        return root
    else:
        return None


class TreeNodeV2:
    """
    We will use this simplified version of TreeNode for the following questions.
    """

    def __init__(
        self,
        val: int,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNodeV2({self.val})"


def distanceK(root, target, k):
    """
    Given the root of a binary tree, a target node, and an integer k,
    return all the values of the nodes that have a distance k from the target node.
    You can return the answer in any order.
        3
       / \
      5   1
     / \  / \
    6  2 0  8
      / \
     7   4
     
    Target: Node with value 5
    k: 2
    Output: [7, 4, 1] — nodes that are 2 edges away from node 5
    """

    # Step 1 - DFS to build a map of node -> parent relationship
    parent_map = {}

    def dfs(node, parent):
        if not node:
            return

        parent_map[node] = parent
        dfs(node.left, node)
        dfs(node.right, node)

    dfs(root, None)

    # Step 2 - BFS from target node
    queue = deque([(target, 0)])
    visited = set([target])

    results = []

    while queue:
        node, dist = queue.popleft()

        if dist == k:
            results.append(node.val)

        elif dist < k:
            # Need to visit left, right children and parent
            for neighbor in [node.left, node.right, parent_map.get(node)]:
                if neighbor and neighbor not in visited:
                    queue.append((neighbor, dist + 1))
                    visited.add(neighbor)

    return results
