import math

from .database import Database
from .model.test_map import TestMap


class Mapping:
    """
    Uses the database to do calculations.

    smallest mean squared error, max delta and match test data.
    """

    def __init__(self, training_index, database):
        """Init the mapping class."""
        self.training_index = training_index
        self.database = database
        self.ideal_index = None
        self.max_delta = None
        self.test_map_list = []

    def __calculate_mean_squared_error(self, ideal_list_index):
        error = 0
        x_y_pairs_length = len(self.database.train_list[self.training_index].x_y_pairs)
        for key, value in self.database.train_list[
            self.training_index
        ].x_y_pairs.items():
            error += (
                value - self.database.ideal_list[ideal_list_index].x_y_pairs[key]
            ) ** 2

        return error / x_y_pairs_length


    def find_smallest_mean_squared_error(self):
        """Find the smallest mean squared error."""
        smallest_mean_squared_error = None

        for ideal_index in range(len(self.database.ideal_list)):
            mean_squared_error = self.__calculate_mean_squared_error(ideal_index)

            if smallest_mean_squared_error is None:
                self.smallest_mean_squared_error = smallest_mean_squared_error = (
                    mean_squared_error
                )
                self.ideal_index = ideal_index

            if mean_squared_error < smallest_mean_squared_error:
                smallest_mean_squared_error = mean_squared_error
                self.ideal_index = ideal_index
                self.smallest_mean_squared_error = smallest_mean_squared_error

        if smallest_mean_squared_error is None:
            error_message = "error: smallest_mean_squared_error could not be calculated"
            raise ValueError(
                error_message,
            )

    def find_matching_test_coordinates(self):
        """Find matching test coordinates."""
        if self.max_delta is None or self.ideal_index is None:
            error_message = """error: max_delta or ideal index is not set,
                               cannot find matching test coordinates"""
            raise ValueError(
                error_message,
            )

        ideal_x_y_pairs = self.database.ideal_list[self.ideal_index].x_y_pairs
        for index in range(len(self.database.test_list)):
            test_x = self.database.test_list[index].point.x
            test_y = self.database.test_list[index].point.y

            delta = abs(ideal_x_y_pairs[test_x] - test_y)

            if delta < (float(self.max_delta) * math.sqrt(2)):
                test_map = TestMap(index, delta)
                self.test_map_list.append(test_map)

    def find_max_delta(self):
        """Find max delta."""
        if self.ideal_index is None:
            error_message = """error: self.index is not set,
                               cannot calculate find_max_delta"""
            raise ValueError(
                error_message,
            )

        max_delta = None

        for key, value in self.database.train_list[
            self.training_index
        ].x_y_pairs.items():
            delta = abs(
                value - self.database.ideal_list[self.ideal_index].x_y_pairs[key],
            )

            if max_delta is None:
                max_delta = delta

            if delta > max_delta:
                max_delta = delta

        if max_delta is None:
            error_message = "error: max delta could not be calculated"
            raise ValueError(error_message)
        self.max_delta = max_delta


if __name__ == "__main__":
    database = Database()
    training_index = 0
    mapping = Mapping(training_index, database)
    mapping.find_smallest_mean_squared_error()
    mapping.find_max_delta()
    mapping.find_matching_test_coordinates()
    print(f"ideal_index: {mapping.ideal_index}")
    print(f"smallest_mean_squared_error: {mapping.smallest_mean_squared_error}")
    print(f"max_delta: {mapping.max_delta}")
    print(f"test_map_list: {mapping.test_map_list}")
