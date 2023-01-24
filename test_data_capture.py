import unittest

from data_capture import DataCapture, UninitializedStats


class TestDataCapture(unittest.TestCase):
    """
    Test cases for DataCapture class
    """

    def setUp(self) -> None:
        """
        Initialize a DataCapture object before each test
        """
        self.data_capture = DataCapture()

    def test_add_valid_number(self):
        """
        Test that a valid number can be added to the numbers list
        """
        self.data_capture.add(10)
        self.assertEqual(self.data_capture.numbers, [10])

    def test_add_invalid_number(self):
        """
        Test that an invalid number (less than 0 or greater than 1000) cannot be added to the numbers list
        """
        self.assertRaises(ValueError, self.data_capture.add, -10)
        self.assertRaises(ValueError, self.data_capture.add, 10000)

    def test_build_stats(self):
        """
        Test that statistics can be built for the numbers list
        """
        self.data_capture.add(10)
        self.data_capture.add(20)
        self.data_capture.build_stats()
        self.assertEqual(self.data_capture.stats[10], (1, 0))
        self.assertEqual(self.data_capture.stats[20], (0, 1))

    def test_build_stats_empty_list(self):
        """
        Test that an error is raised when trying to build statistics for an empty numbers list
        """
        self.assertRaises(ValueError, self.data_capture.build_stats)

    def test_greater(self):
        """
        Test that the correct number of elements greater than a given number can be returned
        """
        self.data_capture.add(10)
        self.data_capture.add(20)
        self.data_capture.build_stats()
        self.assertEqual(self.data_capture.greater(10), 1)

    def test_greater_no_stats(self):
        """
        Test that an error is raised when trying to get greater elements before statistics are built
        """
        self.assertRaises(UninitializedStats, self.data_capture.greater, 10)

    def test_less(self):
        """
        Test that the correct number of elements less than a given number can be returned
        """
        self.data_capture.add(10)
        self.data_capture.add(5)
        self.data_capture.build_stats()
        self.assertEqual(self.data_capture.less(10), 1)

    def test_less_no_stats(self):
        """
        Test that an error is raised when trying to get less elements before statistics are built
        """
        self.assertRaises(UninitializedStats, self.data_capture.less, 10)

    def test_between(self):
        """
        Test that the correct number of elements between a start and end number can be returned
        """
        self.data_capture.add(10)
        self.data_capture.add(20)
        self.data_capture.add(15)
        self.data_capture.build_stats()
        self.assertEqual(self.data_capture.between(10, 15), 2)

    def test_between_invalid_interval(self):
        """
        Test that an error is raised when trying to get elements between an invalid interval
        """
        self.assertRaises(ValueError, self.data_capture.between, 20, 10)

    def test_between_no_stats(self):
        """
        Test that an error is raised when trying to get elements between a start and end number before statistics are built
        """
        self.assertRaises(UninitializedStats, self.data_capture.between, 10, 15)


if __name__ == "__main__":
    unittest.main()
