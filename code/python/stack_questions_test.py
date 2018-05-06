import numpy as np
import unittest

import stack_questions as stack_q


class StackQuestionsTest(unittest.TestCase):

    dump_output = True

    def test_triple_stack(self):

        trip_stack = stack_q.TripleStack(3)
        trip_stack.push(1, 3)
        trip_stack.push(1, 2)

        trip_stack.push(2, 4)
        trip_stack.push(2, 7)

        trip_stack.push(3, 9)
        trip_stack.push(3, 10)

        exp_triple_stack = [3, 2, 0, 4, 7, 0, 9, 10, 0]

        np.testing.assert_array_equal(trip_stack.stacks_array,
                                      exp_triple_stack)

        trip_stack.push(1, 6)
        trip_stack.push(1, 55)

        trip_stack.push(2, 65)
        trip_stack.push(2, 7)

        trip_stack.push(3, 12)

        exp_triple_stack = [3, 2, 6, 4, 7, 65, 9, 10, 12]

        np.testing.assert_array_equal(trip_stack.stacks_array,
                                      exp_triple_stack)

        print('Stack -> ', trip_stack.stacks_array)

        trip_stack.pop(1)
        trip_stack.pop(1)
        trip_stack.pop(1)

        exp_triple_stack = [0, 0, 0, 4, 7, 65, 9, 10, 12]

        np.testing.assert_array_equal(trip_stack.stacks_array,
                                      exp_triple_stack)

        print('Stack -> ', trip_stack.stacks_array)
        trip_stack.pop(2)

        exp_triple_stack = [0, 0, 0, 4, 7, 0, 9, 10, 12]

        np.testing.assert_array_equal(trip_stack.stacks_array,
                                      exp_triple_stack)
        print('Stack -> ', trip_stack.stacks_array)

        trip_stack.pop(3)
        trip_stack.pop(3)
        trip_stack.pop(1)

        exp_triple_stack = [0, 0, 0, 4, 7, 0, 9, 0, 0]

        np.testing.assert_array_equal(trip_stack.stacks_array,
                                      exp_triple_stack)
        print('Stack -> ', trip_stack.stacks_array)


if __name__ == '__main__':
    unittest.main()
