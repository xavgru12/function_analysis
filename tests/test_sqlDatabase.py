import unittest
from unittest.mock import Mock

import sqlDatabase

class TestSqlDatabase(unittest.TestCase):
    def test_init(self):
        command_line_argument_parser = Mock()
 
        args = Mock()
        args.config = "config/database_configuration.json"
        args.csv = None
        command_line_argument_parser.read_arguments.return_value = args 
        
        test_object = sqlDatabase.SqlDatabase(command_line_argument_parser)


        self.assertEqual(test_object.train_dataframe.empty, False)
        self.assertEqual(test_object.ideal_dataframe.empty, False)
        self.assertEqual(test_object.test_dataframe.empty, False)


        #test_object.train_dataframe = Optional[Any]
        #test_object.ideal_dataframe = Optional[Any]
        #test_object.test_dataframe = Optional[Any]
 
        
        # Assert that read_arguments was called
        # mock_parser.read_arguments.assert_called_once()
        
        # Assert that the returned value is used correctly in SqlDatabase
        # This part depends on what SqlDatabase does with the returned value
        # For example, if SqlDatabase stores it in an attribute:
        # self.assertEqual(db.some_attribute, 'expected_value')
        #command_line_argument_parser.read_arguments .assert_called_once()
        #sample_mock.some_method(10)

        #sample_mock.some_method.assert_called_once()

        #create a mock for command line parser and check if read_arguments is called in constructor of sqlDatabase 
        
