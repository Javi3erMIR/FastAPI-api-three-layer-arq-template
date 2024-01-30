from app.repositories.test_repository import TestRepository

class TestService:

    def __init__(self, respository=TestRepository()) -> None:
        self.repo = respository

    def sum_numbers(self, num_one=0.0, num_two=0.0):
        """
        Realices a sum beetween two numbers.

        Args:
        - num_one (int): value of first number.
        - num_two (int): value of second number.

        Returns:
        - int: the value of the sum of two numbers given.
        """
        return num_one + num_two
