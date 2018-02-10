import unittest

import string_manipulation as str_manip


class StringManipulationTest(unittest.TestCase):

    dump_output = True

    def test_rever_str(self):

        input_str = 'Apple'
        exp_str = 'elppA'

        reversed_str = str_manip.reverse_string(input_str)


        revesed_str_2 = str_manip.reverse_string_v2(input_str)


        if self.dump_output:
            print('Original string -> {}'.format(input_str))
            print('Reversed string -> ', reversed_str)

        self.assertEqual(reversed_str, exp_str)

    def test_is_palindrome(self):

        word = 'Mum'
        palin_answer = str_manip.is_palindrome(word)
        if self.dump_output:
            print('Is {} palindrome?'.format(word))
            print('Answer ', palin_answer)

        self.assertTrue(palin_answer)

        word = 'Egg'
        palin_answer = str_manip.is_palindrome(word)
        if self.dump_output:
            print('Is {} palindrome?'.format(word))
            print('Answer ', palin_answer)

        self.assertFalse(palin_answer)

    def test_return_palindrome_subset(self):
        word = 'xolmox'
        exp_subset = 'xoox'
        palin_subset = str_manip.return_palindrome_subset(word)
        if self.dump_output:
            print('Palindrome subset of {}:'.format(word))
            print('Answer ', palin_subset)

        self.assertEqual(palin_subset, exp_subset)


    def test_insertion_sort(self):

        array = [12, 11, 13, 5, 6]

        sorted_arr = str_manip.insertion_sort(array)
        print(sorted_arr)

        string = 'sheep'
        sorted_string = str_manip.sort_input_alphabet(string)
        print(sorted_string)


if __name__ == '__main__':
    unittest.main()
