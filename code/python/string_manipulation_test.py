import unittest

import string_manipulation as str_manip


class StringManipulationTest(unittest.TestCase):

    dump_output = True

    def test_rever_str(self):

        input_str = 'Apple'
        exp_str = 'elppA'

        reversed_str = str_manip.reverse_string_py(input_str)

        self.assertEqual(str_manip.reverse_string(input_str),
                         exp_str)
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

        test_str = "Hey Mel, your uber is arriving now"
        exp_str = ["Hey Mel, your uber,", "is arriving now"]

        #answer = str_manip.breakup_sentence(test_str, 20)

        #self.assertEquals(answer, exp_str)

        #print('Answer is ', answer)

        test_str = "Hey blahblahblah-long named, your uber is arriving now"

        answer = str_manip.breakup_sentence(test_str, 10)


if __name__ == '__main__':
    unittest.main()
