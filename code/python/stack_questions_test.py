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

        trip_stack.pop(1)
        trip_stack.pop(1)
        trip_stack.pop(1)

        exp_triple_stack = [0, 0, 0, 4, 7, 65, 9, 10, 12]

        np.testing.assert_array_equal(trip_stack.stacks_array,
                                      exp_triple_stack)

        trip_stack.pop(2)

        exp_triple_stack = [0, 0, 0, 4, 7, 0, 9, 10, 12]

        np.testing.assert_array_equal(trip_stack.stacks_array,
                                      exp_triple_stack)

        trip_stack.pop(3)
        trip_stack.pop(3)
        trip_stack.pop(1)

        exp_triple_stack = [0, 0, 0, 4, 7, 0, 9, 0, 0]

        np.testing.assert_array_equal(trip_stack.stacks_array,
                                      exp_triple_stack)

        self.assertFalse(trip_stack.is_empty(3))
        self.assertTrue(trip_stack.is_empty(1))

    def test_triple_stackv2(self):

        trip_stack_v2 = stack_q.TripleStackV2(3)
        trip_stack_v2.push(0, 19)

        trip_stack_v2.push(0, 9)
        trip_stack_v2.push(0, 23)
        trip_stack_v2.push(0, 100)

        exp_triple_stack = [19, 9, 23, 100, 0, 0, 0, 0]
        np.testing.assert_array_equal(trip_stack_v2.get_elements(),
                                      exp_triple_stack)

        trip_stack_v2.pop(0)

        trip_stack_v2.push(1, -4)
        trip_stack_v2.push(2, 8)
        trip_stack_v2.push(2, -200)

        exp_triple_stack = [19, 9, 23, -4, 8, -200, 0, 0]
        np.testing.assert_array_equal(trip_stack_v2.get_elements(),
                                      exp_triple_stack)

        trip_stack_v2.pop(1)
        trip_stack_v2.pop(2)

        exp_triple_stack = [19, 9, 23, 0, 8, 0, 0, 0]
        np.testing.assert_array_equal(trip_stack_v2.get_elements(),
                                      exp_triple_stack)

        trip_stack_v2 = stack_q.TripleStackV2(2)
        trip_stack_v2.push(0, 19)
        trip_stack_v2.pop(0)
        trip_stack_v2.pop(0)
        exp_triple_stack = [0, 0, 0, 0, 0]
        np.testing.assert_array_equal(trip_stack_v2.get_elements(),
                                      exp_triple_stack)


if __name__ == '__main__':
    unittest.main()
