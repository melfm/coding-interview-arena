import numpy as np


class TripleStack:
    """Q: Use a single array to implement three stacks.
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
