import numpy as np
import unittest

import probability as probability


class probabilityQuestionsTest(unittest.TestCase):

    def test_prob_more_heads_than_tails(self):

        # 1-based indexing ?
        probs = [0.0, 0.3, 0.4, 0.7]
        N = len(probs)
        output = probability.prob_more_heads_than_tails(probs, N)
        self.assertAlmostEqual(output, 0.442, places=3)


if __name__ == '__main__':
    unittest.main()