"""Generic Tree class."""


class Child:

    def __init__(self, value):
        self.node = TreeNode(value)
        self.next = None

    def add_child(self, node):
        if self.next is None:
            self.next = Child(node)
        else:
            self.next.add_child(node)

    def print_children(self, child, all_values):

        if child is None:
            return

        all_values.append(child.node.value)

        if child.next is None:
            return
        self.print_children(child.next,
                            all_values)


class TreeNode:
    """Generic tree class."""

    def __init__(self, value, children=None):
        self.value = value
        self.children = children

    def add_children(self, node_values):

        for val in node_values:
            if self.children is None:
                self.children = Child(val)
            else:
                self.children.add_child(val)

    def traverse_tree(self, node, all_values=[]):

        if node is None:
            return
        all_values.append(node.value)

        if node.children is None:
            return
        self.traverse_tree(node.children.print_children(node.children,
                                                        all_values))
