import os
import sys
import unittest

sys.path.insert(0, os.getcwd())

from src.entities.torch import Torch


class TestTorchConstructor(unittest.TestCase):
    def test_str(self):
        torch = Torch()
        self.assertIsInstance(torch.color, str)

    def test_null(self):
        torch = Torch(None)
        self.assertTrue(torch.color == "yellow")

    def test_cols(self):
        cols = ["yellow", "blue", "green", "red"]
        for col in cols:
            torch = Torch(col)
            self.assertEqual(col, torch.color)

    def test_valid(self):
        cols = ["lime", "grey"]
        for col in cols:
            with self.assertRaises(ValueError):
                Torch(col)

    def test_type(self):
        cols = ["lime", True, 1.4]
        for col in cols:
            with self.assertRaises(ValueError):
                Torch(col)

if __name__ == "__main__":
    unittest.main()
