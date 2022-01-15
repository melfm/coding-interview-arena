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

        new_nums = maths_q.sample_distribution(numbers, probabilities, 10)
        print('New samples ->', new_nums)

    def test_factorial_trailing_zero(self):

        zero_count = maths_q.factorial_trailing_zero(5)
        self.assertEqual(zero_count, 1)

        zero_count = maths_q.factorial_trailing_zero(28)
        self.assertEqual(zero_count, 6)

        zero_count = maths_q.factorial_trailing_zero(200)
        self.assertEqual(zero_count, 49)

    def test_closest_palindrome_number(self):

        closest_pal = maths_q.closest_palindrome_number(1234)
        self.assertEqual(closest_pal, 1221)

        closest_pal = maths_q.closest_palindrome_number(99)
        self.assertEqual(closest_pal, 101)

        closest_pal = maths_q.closest_palindrome_number(90)
        self.assertEqual(closest_pal, 88)

        closest_pal = maths_q.closest_palindrome_number(121)
        self.assertEqual(closest_pal, [131, 111])

        closest_pal = maths_q.closest_palindrome_number(911)
        self.assertEqual(closest_pal, 909)

        closest_pal = maths_q.closest_palindrome_number(502)
        self.assertEqual(closest_pal, 505)

    def test_orientation3ps(self):
        p1 = maths_q.Point(0, 0)
        p2 = maths_q.Point(4, 4)
        p3 = maths_q.Point(1, 2)

        out = maths_q.orientation3ps(p1, p2, p3)

        print('P1 P2 P3')
        p1.print_coord()
        p2.print_coord()
        p3.print_coord()

        if (out == 0):
            print("Linear")
        elif (out == 1):
            print("Clockwise")
        else:
            print("CounterClockwise")

        p1 = maths_q.Point(0, 0)
        p2 = maths_q.Point(4, 4)
        p3 = maths_q.Point(1, 1)

        out = maths_q.orientation3ps(p1, p2, p3)

        print('\nP1 P2 P3')
        p1.print_coord()
        p2.print_coord()
        p3.print_coord()

        if (out == 0):
            print("Linear")
        elif (out == 1):
            print("Clockwise")
        else:
            print("CounterClockwise")

        print('\n')

    def test_convex_hull(self):

        points = []
        points.append(maths_q.Point(2, 2))
        points.append(maths_q.Point(1, 1))
        points.append(maths_q.Point(2, 1))
        points.append(maths_q.Point(3, 0))
        points.append(maths_q.Point(0, 0))
        points.append(maths_q.Point(3, 3))
        points.append(maths_q.Point(5, 5))
        points.append(maths_q.Point(3, 7))

        # answer = [[0,0], [3,0], [5,5], [3,7]]
        maths_q.convex_hull(points, len(points))


if __name__ == '__main__':
    unittest.main()
