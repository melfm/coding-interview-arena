"""Linked List Questions."""


class Node:

    def __init__(self, value):

        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, value):

        if self.head is None:
            self.head = Node(value)
            self.next = None

        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def pop(self):

        if self.head is None:
            return

        head = self.head
        self.head = self.head.next
        return head.value

    def print_nodes(self):
        head = self.head
        while(head):
            print('Node val: ', head.value)
            head = head.next

    def print_list(self):

        print('Linked List ->')
        self.detect_cycle(print_values=True)
        print('--------------')

    def delete(self, value):
        if self.head.value == value:
            tmp_value = self.head.value
            self.head.value = None
            self.head = self.head.next
            return tmp_value

        current = self.head.next
        while(current):
            if current.value == value:
                tmp_value = current.value
                # do_something

    def detect_cycle(self, print_values=False):
        """Returns true if there is a cycle.
        Store the nodes in a set and do a look up.
        Alternative approach is to store an additional
        visited flag per node.
        """

        table = set()
        current = self.head

        while(current):

            if current in table:
                return True

            table.add(current)
            if print_values:
                print('Node val: ', current.value)
            current = current.next

        return False

    def detect_cycle_v2(self):
        """Floyd's Cycle-Finding algorithm."""

        slow_pointer = self.head
        fast_pointer = self.head

        while(slow_pointer and fast_pointer and fast_pointer.next):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                return True
        return False


def multiply_two_nums(first, second):
    """Multiply two numbers represented by Linked Lists.
        Input : 3->2->1
                1->2
        Output : (321 * 12) = 3852
    """

    num_first = 0
    num_snd = 0

    first_p = first.head
    second_p = second.head

    while(first_p or second_p):

        if first_p:
            num_first = num_first * 10 + first_p.value
            first_p = first_p.next

        if second_p:
            num_snd = num_snd * 10 + second_p.value
            second_p = second_p.next

    return num_first * num_snd
