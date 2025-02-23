import unittest
import heap_questions as heap_qs


class HeapQuestionsTest(unittest.TestCase):

    def test_min_obstacles_to_reach(self):
        grid1 = [
            [0,1,1,0],
            [0,1,0,0],
            [0,0,1,0],
            [1,0,0,0]
        ]

        count = heap_qs.min_obstacles_to_reach(grid1)
        self.assertEqual(count, 0)

        grid2 = [
            [0,1,1,0],
            [0,1,0,0],
            [0,0,1,1],
            [1,0,1,0],
            [1,0,1,0]
        ]

        count = heap_qs.min_obstacles_to_reach(grid2)
        self.assertEqual(count, 1)

        grid3 = [
            [0,1,1,0],
            [1,1,0,1],
            [0,1,1,0],
            [1,0,1,0]
        ]

        count = heap_qs.min_obstacles_to_reach(grid3)
        self.assertEqual(count, 3)

        grid4 = [
            [0,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,0]
        ]

        count = heap_qs.min_obstacles_to_reach(grid4)
        self.assertEqual(count, 5)


    def test_find_smallest_range_k_lists(self):
        list1 = [4, 10, 15, 24, 26]
        list2 = [0, 9, 12, 20]
        list3 = [5, 18, 22, 30]

        expected_output = (20, 24)

        min_range = heap_qs.find_smallest_range_k_lists(list1, list2, list3)
        self.assertEqual(min_range, expected_output)


if __name__ == '__main__':
    unittest.main()