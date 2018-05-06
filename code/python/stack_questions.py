import numpy as np


class TripleStack:
    """Q: Use a single array to implement three stacks.

    Solution: Divide the array in three equal parts and allow
    the individual stack to grow in that limited space.
    """

    def __init__(self, stack_size):
        self.stacks_array = np.empty(stack_size * 3)
        self.stacks_array.fill(0)

        self.stack_size = stack_size
        self.sp1 = -1
        self.sp2 = self.stack_size - 1
        self.sp3 = self.stack_size * 2 - 1

    def push(self, stack_num, value):
        if stack_num == 1:
            if self.sp1 < self.stack_size - 1:
                self.sp1 += 1
                if self.sp1 != self.stack_size:
                    self.stacks_array[self.sp1] = value
                else:
                    self.sp1 -= 1
            else:
                print('Stack is full, cannot add.')
        elif stack_num == 2:
            if self.sp2 <= self.stack_size * 2:
                self.sp2 += 1
                if self.sp2 != self.stack_size * 2:
                    self.stacks_array[self.sp2] = value
                else:
                    self.sp2 -= 1
            else:
                print('Stack is full, cannot add.')

        elif stack_num == 3:
            if self.sp3 <= self.stack_size * 3:

                self.sp3 += 1
                if self.sp3 != self.stack_size * 3:
                    self.stacks_array[self.sp3] = value
                else:
                    self.sp3 -= 1
            else:
                print('Stack is full, cannot add.')

        else:
            raise ValueError('Invalid stack number!')

    def pop(self, stack_num):

        if stack_num == 1:
            value = self.stacks_array[self.sp1]
            if value != 0:
                self.stacks_array[self.sp1] = 0
                self.sp1 -= 1
                return value
            else:
                print('Stack is empty!')

        elif stack_num == 2:
            value = self.stacks_array[self.sp2]
            if value != 0:
                self.stacks_array[self.sp2] = 0
                self.sp2 -= 1
                return value
            else:
                print('Stack is empty!')

        elif stack_num == 3:
            value = self.stacks_array[self.sp3]
            if value != 0:
                self.stacks_array[self.sp3] = 0
                self.sp3 -= 1
                return value
            else:
                print('Stack is empty!')
        else:
            raise ValueError('Invalid stack number!')

    def is_empty(self, stack_num):

        if stack_num == 1:
            if self.stacks_array[0] == 0:
                return True
            else:
                return False

        elif stack_num == 2:
            if self.stacks_array[self.stack_size] == 0:
                return True
            else:
                return False
        elif stack_num == 3:
            if self.stacks_array[self.stack_size * 2] == 0:
                return True
            else:
                return False
        else:
            raise ValueError('Invalid stack number.')


class TripleStackV2:
    """Q: Use a single array to implement three stacks.

    Solution: Any stack can grow as long as there is any free
    space in the array. Note: This code needs error handling
    inside 'push' to avoid overwriting other stack vals.
    """

    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.index_used = 0
        self.stack_pointers = [-1, -1, -1]
        self.stack_array = []

        # Initialize the stacks array with zeros
        self.stack_array = [self.StackNode(0, 0) for i in
                            range(self.stack_size * 3 - 1)]

    class StackNode:

        def __init__(self, previous, value):
            self.previous = previous
            self.value = value

    def push(self, stack_num, value):
        last_index = self.stack_pointers[stack_num]
        self.stack_pointers[stack_num] = self.index_used
        self.index_used += 1
        if self.index_used < self.stack_size * 3:
            self.stack_array[self.stack_pointers[stack_num]] = \
                self.StackNode(last_index, value)
        else:
            print('Stack is full!')

    def pop(self, stack_num):
        if self.stack_pointers[stack_num] == -1:
            print('Stack is empty.')
            return

        out_value = self.stack_array[self.stack_pointers[stack_num]].value
        last_index = self.stack_pointers[stack_num]

        self.stack_pointers[stack_num] = self.stack_array[
            self.stack_pointers[stack_num]].previous

        self.stack_array[last_index] = self.StackNode(0, 0)
        self.index_used -= 1

        return out_value

    def print_stack(self):

        elements = self.get_elements()
        print('Stack pointers -> ,', self.stack_pointers)
        print('Stack ->', elements)

    def get_elements(self):
        elements = []
        for i in range(len(self.stack_array)):
            value = self.stack_array[i].value
            elements.append(value)

        return elements
