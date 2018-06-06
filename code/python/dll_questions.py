"""Doubly Linked List Questions."""


class DoublyLinkedList:

    class Node:

        def __init__(self, data):

            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_front(self, data):
        pass

    def insert_at_end(self, data):

        node = self.Node(data)
        last = self.head

        if self.head is None:
            self.head = node
            return

        else:
            while(last.next is not None):
                last = last.next

        last.next = node
        node.prev = last

    def get_nodes(self):
        head = self.head
        node_list = []
        while(head):
            node_list.append(head.data)
            head = head.next
        return node_list

    def insert_after_node(self, prev_node, data):
        pass

    def insert_before_node(self, next_node, data):
        pass
