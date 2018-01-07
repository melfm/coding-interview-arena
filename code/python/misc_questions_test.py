import unittest

import misc_questions as misc


class StringManipulationTest(unittest.TestCase):

    dump_output = True

    def test_isPowOf3(self):

        self.assertFalse(misc.isPowerOf3_loop(10))

        self.assertTrue(misc.isPowerOf3_int_limit(27))

        self.assertTrue(misc.isPowerOf3_recursive(27))
        self.assertFalse(misc.isPowerOf3_recursive(10))


if __name__ == '__main__':
    unittest.main()
