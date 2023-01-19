import numpy as np


class DataCapture:
    def __init__(self) -> None:
        self.numbers = []
        self.stats = {}

    def validate_element(self, number: int) -> None:
        if number < 0 or number > 1000:
            raise ValueError("Only positive numbers allowed")

    def add(self, number: int) -> None:
        self.validate_element(number)
        self.numbers.append(number)

    def build_stats(self) -> None:
        numbers = range(0, 1001)
        np_numbers = np.array(self.numbers)
        self.stats = {
            num: (np_numbers[np_numbers > num].size, np_numbers[np_numbers < num].size)
            for num in numbers
        }

    def greater(self, number: int) -> int:
        self.validate_element(number)
        if not self.stats:
            raise AttributeError("Please execute build_stats")
        return self.stats[number][0]

    def less(self, number: int) -> int:
        self.validate_element(number)
        if not self.stats:
            raise AttributeError("Please execute build_stats")
        return self.stats[number][1]

    def between(self, start_number: int, end_number: int) -> int:
        self.validate_element(start_number)
        self.validate_element(end_number)
        if not self.stats:
            raise AttributeError("Please execute build_stats")
        return len(self.numbers) - self.greater(end_number) - self.less(start_number)
