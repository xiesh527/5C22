from Median_filter import *
from cubic_spline_fil import *
import numpy as np
import unittest


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(check_odd(3), 1)
        self.assertEqual(f_odd(3), [1, 3, 5])
        self.assertEqual(median_fil([1, 8, 3], 3), [4, 3, 4])
        # Using mean as the padded number
        self.assertEqual(get_padding(3, [1, 4, 1]), [2, 1, 4, 1, 2])
        self.assertEqual(median_fil([1, 2, 3, 4, 99, 6, 7], 3), [
                         2, 2, 3, 4, 6, 7, 7])
        self.assertEqual(report_index([0, 1, 1, 0]), [1, 2])
        # I do not know to type data like [1 1] in python, hence the result need to be converted to list first
        self.assertEqual(
            (tick_out_clips([1, 2], [1, 99, 99, 1])).tolist(), [1, 1])
        self.assertEqual(tick_out_clips_index([0, 1, 2, 3, 4, 5], [1, 2]).tolist(), [0, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
