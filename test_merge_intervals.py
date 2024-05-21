import unittest
from merge_intervals import merge_intervals


class TestMergeIntervals(unittest.TestCase):
    def test_merge_intervals(self):
        self.assertEqual(merge_intervals([[0, 300], [600, 1200], [3500, 6000]], threshold=400), [[0, 1200], [3500, 6000]])
        self.assertEqual(merge_intervals([[0, 300], [600, 1200], [3500, 6000]], threshold=100), [[0, 300], [600, 1200], [3500, 6000]])
        self.assertEqual(merge_intervals([[0, 300], [600, 1200], [3500, 6000]], threshold=2500), [[0, 6000]])

if __name__ == '__main__':
    unittest.main()
