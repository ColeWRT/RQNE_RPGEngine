#!/usr/bin/env python3

import unittest
import circles
import numpy as np

class TestFunctions(unittest.TestCase):
    def test_circumference(self):
        self.assertAlmostEqual(circles.circumference(1), 2 * np.pi)
        self.assertAlmostEqual(circles.circumference(0), 0)
        self.assertAlmostEqual(circles.circumference(2.5), 2 * np.pi * 2.5)

    def test_area(self):
        self.assertAlmostEqual(circles.area(1), np.pi)
        self.assertAlmostEqual(circles.area(0), 0)
        self.assertAlmostEqual(circles.area(2.5), np.pi * 2.5 * 2.5)

if __name__ == "__main__":
    unittest.main()