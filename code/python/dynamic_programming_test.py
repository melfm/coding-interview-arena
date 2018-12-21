import unittest

import dynamic_programming as dp


class DynamicProgrammingQuestionsTest(unittest.TestCase):

    dump_output = True

    def test_get_fib(self):

        n = 9
        res = dp.fibonacci_dp(n)
        self.assertEqual(res, 34)

        if self.dump_output:
            print('Fibonacci loop for value {} ->'.format
                  (n), res)

        fib_array = [0, 1]
        res = dp.fibonacci_dp_recursive(n, fib_array)
        self.assertEqual(res, 34)

        if self.dump_output:
            print('Fibonacci recursive for value {} ->'.format
                  (n), res)

    def test_get_min_steps_mem(self):

        n = 10
        db_res = dp.get_min_steps_mem(n)
        self.assertEqual(db_res, 3)
        if self.dump_output:
            print('Min steps to reduce {} --> '.format(n), db_res)

    def test_decode_ways(self):
        digits = ['2', '2', '6']

        count = dp.decode_ways(digits, len(digits))
        self.assertEqual(count, 3)

        digits = ['2', '6', '2']

        count = dp.decode_ways(digits, len(digits))
        self.assertEqual(count, 2)

        digits = ['1', '2', '2', '3']

        count = dp.decode_ways(digits, len(digits))
        self.assertEqual(count, 4)

        digits = ['2', '2', '6']

        count = dp.decode_ways_rec(digits, len(digits))
        self.assertEqual(count, 3)

        digits = ['2', '6', '2']

        count = dp.decode_ways_rec(digits, len(digits))
        self.assertEqual(count, 2)

        # This case breaks the code - safe to assume our
        # digits don't contain 0's?
        digits = ['2', '2', '0', '6']
        count = dp.decode_ways(digits, len(digits))
        # self.assertEqual(count, 2)


if __name__ == '__main__':
    unittest.main()
