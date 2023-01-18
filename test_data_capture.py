import unittest

from data_capture import DataCapture


class TestDataCapture(unittest.TestCase):
    def setUp(self) -> None:
        numbers = [3, 9, 3, 4, 6, 5]
        self.data_capture = DataCapture(numbers)

    def test_empty_init(self):
        data_capture = DataCapture()
        data_capture.add(5)
        data_capture.add(6)
        data_capture.add(3)
        data_capture.add(4)
        data_capture.add(9)

    def test_positive_numbers(self):
        self.data_capture.add(10)
        self.assertEqual(self.data_capture.numbers.size, 7)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            self.data_capture.add(-203)

    def test_exceptiom_stats(self):
        with self.assertRaises(AttributeError):
            self.data_capture.greater(8)
            self.data_capture.less(7)
            self.data_capture.between(8)

    def test_stats(self):
        self.data_capture.build_stats()
        self.assertEqual(self.data_capture.greater(2), 6)
        self.assertEqual(self.data_capture.less(7), 5)
        self.assertEqual(self.data_capture.between(2, 6), 5)


if __name__ == "__main__":
    unittest.main()
