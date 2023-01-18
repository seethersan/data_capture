import numpy as np


class DataCapture:
    def __init__(self, numbers: list[int] = []) -> None:
        numbers = np.array(numbers)
        if numbers[numbers < 0].size > 0:
            raise ValueError("Only positive numbers allowed")
        self.numbers = numbers

    def validate_element(self, number: int) -> None:
        if number < 0 or number > 1000:
            raise ValueError("Only positive numbers allowed")

    def add(self, number: int) -> None:
        self.validate_element(number)
        self.numbers = np.append(self.numbers, number)

    def build_stats(self) -> None:
        numbers = range(1, 1001)
        self.greater_numbers = {
            num: self.numbers[self.numbers > num].size for num in numbers
        }
        self.less_numbers = {
            num: self.numbers[self.numbers < num].size for num in numbers
        }

    def greater(self, number: int) -> int:
        self.validate_element(number)
        if not hasattr(self, "greater_numbers"):
            raise AttributeError("Please execute build_stats")
        return self.greater_numbers[number]

    def less(self, number: int) -> int:
        self.validate_element(number)
        if not hasattr(self, "less_numbers"):
            raise AttributeError("Please execute build_stats")
        return self.less_numbers[number]

    def between(self, start_number: int, end_number: int) -> int:
        self.validate_element(start_number)
        if not hasattr(self, "greater_numbers") or not hasattr(self, "less_numbers"):
            raise AttributeError("Please execute build_stats")
        return self.numbers.size - self.greater(end_number) - self.less(start_number)
