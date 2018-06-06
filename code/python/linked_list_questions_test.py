import unittest

import linked_list_questions as linked_list


class LinkedListQuestionsTest(unittest.TestCase):

    dump_output = True

    def test_insert(self):

        test_list = linked_list.LinkedList()
        test_list.push(2)
        test_list.push(5)
        test_list.push(7)

        if self.dump_output:
            test_list.print_list()

        test_list.pop()
        test_list.pop()
        if self.dump_output:
            test_list.print_list()

    def test_detect_cycle(self):
        test_list = linked_list.LinkedList()
        test_list.push(2)
        test_list.push(5)
        test_list.push(7)

        self.assertFalse(test_list.detect_cycle())
        self.assertFalse(test_list.detect_cycle_v2())

        # Manually create a cycle for testing
        test_list.head.next.next.next = test_list.head

        self.assertTrue(test_list.detect_cycle())
        self.assertTrue(test_list.detect_cycle_v2())

        # Add more elemenets
        test_list.push(10)
        test_list.push(9)
        test_list.push(18)
        if self.dump_output:
            print('Test case: detect cycle')
            test_list.print_list()

        self.assertTrue(test_list.detect_cycle())
        self.assertTrue(test_list.detect_cycle_v2())

    def test_multiply_two_nums(self):
        first_list = linked_list.LinkedList()
        # Note: Since this is a SLL, we need to add
        # the numbers in reverse. The list we want is
        # [3, 2, 1]. Could use DLL.insert_at_end instead to
        # preserve the order.
        first_list.push(1)
        first_list.push(2)
        first_list.push(3)

        second_list = linked_list.LinkedList()
        second_list.push(2)
        second_list.push(1)

        mult_res = linked_list.multiply_two_nums(first_list,
                                                 second_list)

        self.assertEqual(mult_res, 3852)

        first_list = linked_list.LinkedList()
        first_list.push(6)
        first_list.push(4)
        first_list.push(9)

        second_list = linked_list.LinkedList()
        second_list.push(4)
        second_list.push(8)

        mult_res = linked_list.multiply_two_nums(first_list,
                                                 second_list)

        self.assertEqual(mult_res, 79464)


if __name__ == '__main__':
    unittest.main()
