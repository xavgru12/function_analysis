import unittest
from unittest.mock import Mock, patch
import pandas

from src.mapping import Mapping 

class TestMapping(unittest.TestCase):
    def setUp(self):
        self.database = Mock()
        self.setup_mock()

    def setup_mock(self):

        train = Mock()
        train.x_y_pairs = {1:10, 2:11, 3:11}
        
        ideal = Mock()
        ideal.x_y_pairs = {1:10, 2:11, 3:12}

        
        self.test_first_matching = Mock()
        self.test_first_matching.point.x = 1 
        self.test_first_matching.point.y = 11 


        self.test_not_matching = Mock()
        self.test_not_matching.point.x = 1 
        self.test_not_matching.point.y = 20


        self.test_second_matching = Mock()
        self.test_second_matching.point.x = 1 
        self.test_second_matching.point.y = 9.8 

        self.database.train_list = [train] 
        self.database.ideal_list = [ideal] 

    def test_find_smallest_mean_squared_error(self):

        mapping = Mapping(0, self.database)
        mapping.find_smallest_mean_squared_error()
        self.assertEqual(mapping.smallest_mean_squared_error, 1/3)

    def test_find_max_delta(self):

        mapping = Mapping(0, self.database)
        mapping.find_smallest_mean_squared_error()
        mapping.find_max_delta()
        self.assertEqual(mapping.max_delta, 1)

    def test_find_matching_test_coordinates(self):

        self.database.test_list = [self.test_first_matching]

        mapping = Mapping(0, self.database)
        mapping.find_smallest_mean_squared_error()
        mapping.find_max_delta()
        mapping.find_matching_test_coordinates()
        self.assertEqual(mapping.test_map_list[0].test_list_index, 0)
        self.assertEqual(mapping.test_map_list[0].delta, 1)

        self.assertEqual(len(mapping.test_map_list), 1)

    def test_not_matching_coordinates(self):

        self.database.test_list = [self.test_first_matching, self.test_not_matching]

        mapping = Mapping(0, self.database)
        mapping.find_smallest_mean_squared_error()
        mapping.find_max_delta()
        mapping.find_matching_test_coordinates()

        self.assertEqual(len(mapping.test_map_list), 1)

    def test_two_matching_coordinates(self):

        self.database.test_list = [self.test_first_matching, self.test_second_matching, self.test_not_matching]

        mapping = Mapping(0, self.database)
        mapping.find_smallest_mean_squared_error()
        mapping.find_max_delta()
        mapping.find_matching_test_coordinates()

        self.assertEqual(len(mapping.test_map_list), 2)

