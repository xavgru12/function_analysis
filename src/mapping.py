from .database import Database
from .model.test_map import TestMap
import math

class Mapping:
    def __init__(self, training_index, database):
        self.training_index = training_index
        self.database = database
        self.ideal_index = None
        self.max_delta = None
        self.test_map_list = [] 

    def calculate_mean_squared_error(self, ideal_list_index):
        error = 0
        x_y_pairs_length = len(self.database.train_list[self.training_index].x_y_pairs)
        for key, value in self.database.train_list[self.training_index].x_y_pairs.items():
            error += (value - self.database.ideal_list[ideal_list_index].x_y_pairs[key]) ** 2
        #breakpoint()
        mean_squared_error = error / x_y_pairs_length
        return mean_squared_error

    def find_smallest_mean_squared_error(self):

        smallest_mean_squared_error = None 

        for ideal_index in range(len(self.database.ideal_list)):
            mean_squared_error = self.calculate_mean_squared_error(ideal_index)

            if smallest_mean_squared_error == None:
                self.smallest_mean_squared_error = smallest_mean_squared_error = mean_squared_error
                self.ideal_index = ideal_index

            if mean_squared_error < smallest_mean_squared_error:
                smallest_mean_squared_error = mean_squared_error
                self.ideal_index = ideal_index
                self.smallest_mean_squared_error = smallest_mean_squared_error
        
        if smallest_mean_squared_error == None:
            raise ValueError("error: smallest_mean_squared_error could not be calculated")


    def find_matching_test_coordinates(self):

        if self.max_delta is None or self.ideal_index is None:
            raise ValueError("error: max_delta or ideal index is not set, cannot find matching test coordinates")

        ideal_x_y_pairs = self.database.ideal_list[self.ideal_index].x_y_pairs 
        for index in range(len(self.database.test_list)):
            test_x = self.database.test_list[index].point.x 
            test_y = self.database.test_list[index].point.y 

            delta = abs(ideal_x_y_pairs[test_x] - test_y) 
                
            if delta < (float(self.max_delta) * math.sqrt(2)): 
                test_map = TestMap(index, delta)
                self.test_map_list.append(test_map)


    def find_max_delta(self):

        if self.ideal_index == None:
            raise ValueError("error: self.index is not set, cannot calculate find_max_delta")

        max_delta = None

        for key, value in self.database.train_list[self.training_index].x_y_pairs.items():
            delta = abs(value - self.database.ideal_list[self.ideal_index].x_y_pairs[key])

            if max_delta == None:
                max_delta = delta

            if delta > max_delta:
               max_delta = delta  

        if max_delta == None:
            raise ValueError("error: max delta could not be calculated")
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
