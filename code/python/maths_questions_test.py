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


if __name__ == '__main__':
    unittest.main()
