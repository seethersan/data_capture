from collections import Counter


class UninitializedStats(Exception):
    """Raises an exception when build_stats is empty yet"""


class DataCapture:
    """
    DataCapture class captures the data and provides statistics of the data.

    This class provides methods to add, validate and build statistics of numbers. It also provides methods to
    check for the number of elements greater, less than and between the given number.

    Attributes:
    numbers (list): A list of numbers
    stats (dict): A dictionary containing the statistics of numbers
    """

    def __init__(self) -> None:
        """
        Initializes an instance of the class, creating an empty list for numbers and an empty dictionary for stats.
        """
        self.numbers = []
        self.numbers_len = 0
        self.stats = {}

    def validate_element(self, number: int) -> None:
        """
        Validate the input number is an integer and within the allowed range.

        Parameters:
        number (int): The number to be validated

        Raises:
        ValueError: If the number is not an integer or if the number is less than 0 or greater than 1000.
        """
        if type(number) != int:
            raise ValueError("Only integers allowed")
        if number < 0 or number > 1000:
            raise ValueError("Only positive numbers allowed")

    def add(self, number: int) -> None:
        """
        Add a number to the list of numbers.

        Parameters:
        number (int): The number to be added to the list

        Raises:
        ValueError: If the number is not an integer or if the number is less than 0 or greater than 1000.
        """
        self.validate_element(number)
        self.numbers.append(number)
        self.numbers_len += 1

    def build_stats(self) -> None:
        """
        Build statistics of numbers.

        Build a dictionary containing the number of elements in the list that are greater than and less than
        each number between 0 and 1000.

        Raises:
        ValueError: If the list of numbers is empty.
        """
        if self.numbers_len == 0:
            raise ValueError("Empty number list, please add values")

        count = [0] * 1001
        for num in self.numbers:
            count[num] += 1
        self.stats = {}
        for i in range(1, 1001):
            count[i] += count[i - 1]
        for i in range(1000, -1, -1):
            self.stats[i] = (count[1000] - count[i], count[i - 1])

    def greater(self, number: int) -> int:
        """
        Get the number of elements in the list that are greater than the given number.

        Parameters:
        number (int): The number to compare the list elements against

        Raises:
        ValueError: If the number is not an integer or if the number is less than 0 or greater than 1000.
        UninitializedStats: If the statistics have not been built yet

        Returns:
        int: The number of elements in the list that are greater than the given number
        """
        self.validate_element(number)
        if not self.stats:
            raise UninitializedStats("Please execute build_stats")
        return self.stats[number][0]

    def less(self, number: int) -> int:
        """
        Get the number of elements in the list that are less than the given number.

        Parameters:
        number (int): The number to compare the list elements against

        Raises:
        ValueError: If the number is not an integer or if the number is less than 0 or greater than 1000.
        UninitializedStats: If the statistics have not been built yet

        Returns:
        int: The number of elements in the list that are greater than the given number
        """
        self.validate_element(number)
        if not self.stats:
            raise UninitializedStats("Please execute build_stats")
        return self.stats[number][1]

    def between(self, start_number: int, end_number: int) -> int:
        """
        Get the number of elements in the list that are between the start and end number.

        Parameters:
        start_number (int): The start number of the interval
        end_number (int): The end number of the interval

        Raises:
        ValueError: If the start_number is greater than the end_number, if the start_number or end_number is not an integer or if the start_number or end_number is less than 0 or greater than 1000.
        UninitializedStats: If the statistics have not been built yet

        Returns:
        int: The number of elements in the list that are between the start and end number
        """
        self.validate_element(start_number)
        self.validate_element(end_number)
        if start_number > end_number:
            raise ValueError("Please insert valid interval")
        if not self.stats:
            raise UninitializedStats("Please execute build_stats")
        return self.numbers_len - self.greater(end_number) - self.less(start_number)


if __name__ == "__main__":
    """
    Main function to test the DataCapture class.
    """
    data_capture = DataCapture()
    data_capture.add(1)
    data_capture.add(2)
    data_capture.add(2)
    data_capture.add(2)
    data_capture.add(5)
    data_capture.add(7)
    data_capture.add(7)
    data_capture.add(7)
    data_capture.add(9)
    data_capture.add(10)
    data_capture.build_stats()
    print(data_capture.greater(5))
    print(data_capture.less(5))
    print(data_capture.between(5, 10))
