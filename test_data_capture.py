import unittest

from data_capture import DataCapture


class TestDataCapture(unittest.TestCase):
    def setUp(self) -> None:
        self.data_capture = DataCapture()
        self.data_capture.add(3)
        self.data_capture.add(9)
        self.data_capture.add(3)
        self.data_capture.add(4)
        self.data_capture.add(6)
        self.data_capture.add(5)

    def test_positive_numbers(self):
        self.data_capture.add(10)
        self.assertEqual(len(self.data_capture.numbers), 7)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            self.data_capture.add(-203)

    def test_exception_stats(self):
        with self.assertRaises(AttributeError):
            self.data_capture.greater(8)
            self.data_capture.less(7)
            self.data_capture.between(8)

    def test_stats(self):
        self.data_capture.build_stats()
        self.assertEqual(self.data_capture.greater(2), 6)
        self.assertEqual(self.data_capture.less(7), 5)
        self.assertEqual(self.data_capture.between(2, 6), 5)

    def test_invalid_stats(self):
        self.data_capture.build_stats()
        with self.assertRaises(ValueError):
            self.data_capture.greater(-2)
            self.data_capture.less(1001)
            self.data_capture.between(-4, 2032)


if __name__ == "__main__":
    unittest.main()
