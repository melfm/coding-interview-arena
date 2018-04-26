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


if __name__ == '__main__':
    unittest.main()
