import unittest

import dll_questions as dll


class DoublyLinkedListQuestionsTest(unittest.TestCase):

    dump_output = True

    def test_insert_at_end(self):
        test_list = dll.DoublyLinkedList()
        test_list.insert_at_end(2)
        test_list.insert_at_end(5)
        test_list.insert_at_end(7)

        exp_node_order = [2, 5, 7]
        self.assertEqual(test_list.get_nodes(), exp_node_order)


if __name__ == '__main__':
    unittest.main()
