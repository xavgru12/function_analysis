import unittest
from unittest.mock import Mock, patch
import pandas

from src.database import Database 

class TestDatabase(unittest.TestCase):
    def test_read_from_sql_database(self):
        sql_database = Mock()

        train = {
          "x": [1, 2, 3],
          "y1": [10, 11, 12],
          "y2": [20, 21, 22],
          "y3": [30, 31, 32],
          "y4": [40, 41, 42]
        }
        train_dataframe = pandas.DataFrame(train)

        ideal = {
          "x": [4, 5, 6],
          "y1": [10, 11, 12],
          "y2": [20, 21, 22],
          "y3": [30, 31, 32],
          "y4": [40, 41, 42]
        }
        ideal_dataframe = pandas.DataFrame(ideal)

        test = {
          "x": [7, 8, 9],
          "y": [10, 11, 12]
        }
        test_dataframe = pandas.DataFrame(test)

        sql_database.train_dataframe = train_dataframe 
        sql_database.test_dataframe = test_dataframe 
        sql_database.ideal_dataframe = ideal_dataframe 

        database = Database(sql_database)

        self.assertEqual(database.train_list[0].x_y_pairs, {1:10, 2:11, 3:12})
        self.assertEqual(database.ideal_list[0].x_y_pairs, {4:10, 5:11, 6:12})
        self.assertEqual(database.test_list[0].point.x, 7)
        self.assertEqual(database.test_list[0].point.y, 10)

