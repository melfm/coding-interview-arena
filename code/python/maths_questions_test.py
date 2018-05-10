import unittest

import maths_questions as maths_q


class MathsQuestionsTest(unittest.TestCase):

    def test_divisible_by_r(self):

        answer = maths_q.divisible_by_r(4, 6)
        self.assertEqual(answer, 12)

        answer = maths_q.divisible_by_r(55, 40)
        self.assertEqual(answer, 440)

    def test_generate_rand_7(self):

        ans = maths_q.generate_rand_7()
        print('Random number -> ', ans)

    def test_sample_distribution(self):

        numbers = [1, 2, 3, 4]
        probabilities = [0.1, 0.2, 0.3, 0.4]

        new_nums = maths_q.sample_distribution(numbers,
                                               probabilities,
                                               10)
        print('New samples ->', new_nums)


if __name__ == '__main__':
    unittest.main()
