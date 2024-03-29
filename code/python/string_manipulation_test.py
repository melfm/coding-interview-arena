import numpy as np
import random
import string
import time
import unittest

import string_manipulation as str_manip


class StringManipulationTest(unittest.TestCase):

    dump_output = False
    test_runtime = True

    def test_rever_str(self):

        input_str = 'Apple'
        exp_str = 'elppA'

        reversed_str = str_manip.reverse_string_py(input_str)

        self.assertEqual(str_manip.reverse_string(input_str), exp_str)
        if self.dump_output:
            print('Original string -> {}'.format(input_str))
            print('Reversed string -> ', reversed_str)

        self.assertEqual(reversed_str, exp_str)

    def test_is_palindrome(self):

        word = 'Mum'
        palin_answer = str_manip.is_palindrome(word)
        if self.dump_output:
            print('Is {} palindrome?'.format(word), ' -> Answer: ',
                  palin_answer)

        self.assertTrue(palin_answer)

        word = 'Egg'
        palin_answer = str_manip.is_palindrome(word)
        if self.dump_output:
            print('Is {} palindrome?'.format(word), ' -> Answer: ',
                  palin_answer)

        self.assertFalse(palin_answer)

    def test_return_palindrome_subset(self):
        word = 'xolmox'
        exp_subset = 'xoox'
        palin_subset = str_manip.return_palindrome_subset(word)
        if self.dump_output:
            print('Palindrome subset of {}:'.format(word), '-> Answer ',
                  palin_subset)

        self.assertEqual(palin_subset, exp_subset)

    def test_string_anagram(self):

        string_a = 'abcd'
        string_b = 'dabc'

        self.assertTrue(str_manip.string_anagram_loop(string_a, string_b))

        self.assertTrue(str_manip.string_anagram_count(string_a, string_b))

        string_a = 'abcd'
        string_b = 'daacd'

        self.assertFalse(str_manip.string_anagram_loop(string_a, string_b))
        self.assertFalse(str_manip.string_anagram_count(string_a, string_b))

        string_a = 'listen'
        string_b = 'silent'

        self.assertTrue(str_manip.string_anagram_loop(string_a, string_b))
        self.assertTrue(str_manip.string_anagram_count(string_a, string_b))

    def test_string_has_unique_chars(self):

        test_str = 'abcde'
        self.assertTrue(str_manip.string_has_unique_chars(test_str))

        test_str = 'abcdeaa'
        self.assertFalse(str_manip.string_has_unique_chars(test_str))

        test_str = 'abcd'
        self.assertTrue(str_manip.string_has_unique_chars_v2(test_str))

        test_str = 'aaabbcc'
        self.assertFalse(str_manip.string_has_unique_chars_v2(test_str))

    def test_breakup_sentence(self):

        test_str = 'Hey Mel, your uber is arriving now'
        exp_str = ['Hey Mel, your uber', 'is arriving now']

        answer = str_manip.breakup_sentence(test_str, 20)

        np.testing.assert_array_equal(np.asarray(answer), np.asarray(exp_str))

        test_str = 'Hey blahblahblah-long named, your uber is arriving now'

        exp_str = [
            'Hey', 'blahblahbl', 'ah-long', 'named, your uber', 'is arriving',
            'now'
        ]

        answer = str_manip.breakup_sentence(test_str, 10)
        np.testing.assert_array_equal(np.asarray(answer), np.asarray(exp_str))

    def test_find_matching_brackets(self):

        input_string = '()(())'
        long_match = str_manip.find_matching_brackets(input_string)
        self.assertEqual(long_match, 4)

        input_string = ')()((())(()'
        long_match = str_manip.find_matching_brackets(input_string)
        self.assertEqual(long_match, 4)

        input_string = ')()((()))(()'
        long_match = str_manip.find_matching_brackets(input_string)
        self.assertEqual(long_match, 6)

    def test_combine_and_permute(self):

        input_string = ['a', 'b', 'c']
        exp_combinations = [['a'], ['a', 'b'], ['b', 'a'], ['a', 'b', 'c'],
                            ['a', 'c', 'b'], ['b', 'a', 'c'], ['b', 'c', 'a'],
                            ['c', 'b', 'a'], ['c', 'a', 'b'], ['a', 'c'],
                            ['c', 'a'], ['b'], ['b', 'c'], ['c', 'b'], ['c']]
        combinations = str_manip.combine_and_permute(input_string)
        self.assertEqual(combinations, exp_combinations)
        if self.dump_output:
            print('Permutation combinations -> \n', combinations)

    def test_combine_and_permute_order_free(self):

        input_string = ['a', 'b', 'c']
        exp_combinations = ['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
        combinations = str_manip.combine_and_permute_order_free_str(
            input_string)
        self.assertEqual(combinations, exp_combinations)

    def test_remove_str_mask_char(self):

        input_string = "Samplestring"
        str_mask = "msg"
        exp_string = "apletrin"

        output = str_manip.remove_str_mask_char(input_string, str_mask)
        self.assertEqual(output, exp_string)

    def test_remove_str_mask_char_v2(self):

        input_string = "Samplestring"
        str_mask = "msg"
        exp_string = "apletrin"

        output = str_manip.remove_str_mask_char_v2(input_string, str_mask)
        self.assertEqual(output, exp_string)

        input_string = "This is a setence containing stuff!"
        str_mask = "msffc"
        exp_string = "thi i a etene ontaining tu!"

        output = str_manip.remove_str_mask_char_v2(input_string, str_mask)
        self.assertEqual(output, exp_string)

        if self.test_runtime:

            count = 100000
            random_str = ''.join(
                random.choice(string.ascii_lowercase) for x in range(count))
            random_mask = ''.join(
                random.choice(string.ascii_lowercase) for x in range(10))

            start = time.time()
            output = str_manip.remove_str_mask_char(random_str, random_mask)
            # print('\nremove_str_mask_char took ', time.time() - start)

            start = time.time()
            output = str_manip.remove_str_mask_char_v2(random_str, random_mask)
            # print('\nremove_str_mask_char_v2 took ', time.time() - start)

    def test_isEditDistanceOne(self):
        str1 = "cat"
        str2 = "cats"

        output = str_manip.isEditDistanceOne(str1, str2)
        self.assertTrue(output)

        str1 = "cat"
        str2 = "at"

        output = str_manip.isEditDistanceOne(str1, str2)
        self.assertTrue(output)

        str1 = "cat"
        str2 = "dog"
        output = str_manip.isEditDistanceOne(str1, str2)
        self.assertFalse(output)

        str1 = "cat"
        str2 = "cut"

        output = str_manip.isEditDistanceOne(str1, str2)
        self.assertTrue(output)

    def test_k_palindrome(self):

        input_str = "abxa"
        k = 1
        output = str_manip.k_palindrome(input_str, k)
        self.assertTrue(output)

        input_str = "abdxa"
        k = 1
        output = str_manip.k_palindrome(input_str, k)
        self.assertFalse(output)

        input_str = "abxwza"
        k = 3
        output = str_manip.k_palindrome(input_str, k)
        self.assertTrue(output)

    def test_longest_unique_substring(self):

        input_str = "pwwkew"
        output = str_manip.longest_unique_substring_v2(input_str)
        exp_subs = ['wke', 'kew']
        self.assertEqual(output, exp_subs)

    def test_remove_duplicate_char_order(self):

        input_str = "bcabc"
        exp_string = "abc"

        output = str_manip.remove_duplicate_char_order(input_str)
        self.assertEqual(output, exp_string)

        input_str = "cbacdcbc"
        exp_string = "acdb"
        output = str_manip.remove_duplicate_char_order(input_str)
        self.assertEqual(output, exp_string)

    def test_isInterleave(self):

        # input_str1 = "aabcc"
        # input_str2 = "dbbca"
        # output_str = "aadbbcbcac"

        # output = str_manip.isInterleave(input_str1, input_str2, output_str)

        # self.assertTrue(output)

        input_str1 = "aabcc"
        input_str2 = "dbbca"
        output_str = "aadbbbaccc"

        output = str_manip.isInterleave(input_str1, input_str2, output_str)

        self.assertFalse(output)

if __name__ == '__main__':
    unittest.main()
