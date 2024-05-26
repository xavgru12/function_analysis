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

    def test_init_write(self):
        command_line_argument_parser = Mock()
 
        args = Mock()
        args.config = "config/database_configuration.json"
        args.csv = "data"
        command_line_argument_parser.read_arguments.return_value = args 
        
        test_object = sqlDatabase.SqlDatabase(command_line_argument_parser)


        self.assertEqual(test_object.train_dataframe.empty, False)
        self.assertEqual(test_object.ideal_dataframe.empty, False)
        self.assertEqual(test_object.test_dataframe.empty, False)

