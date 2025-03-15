import numpy as np
import unittest

import interval_questions as inter


class IntervalQuestionsTest(unittest.TestCase):

    dump_output = False

    def test_aggregate_intervals(self):

        # ---------------------------
        # Example with your input:
        # ---------------------------
        input_ranges = [
            [[0, 4], [25, 30]],  # Labeler 1
            [[1, 5], [25, 35]],  # Labeler 2
            [[0, 7]]             # Labeler 3
        ]
        intervals = inter.aggregate_intervals(input_ranges)
        expected = [(1, 4), (25, 30)]
        self.assertEqual(sorted(expected), sorted(intervals))


if __name__ == '__main__':
    unittest.main()