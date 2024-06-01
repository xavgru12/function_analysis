import unittest
from unittest.mock import Mock, patch
import pandas

import sqlDatabase

class TestSqlDatabase(unittest.TestCase):
    @patch('sqlalchemy.create_engine')
    @patch('sqlDatabase.pandas.read_sql_table')
    @patch('sqlDatabase.sqlalchemy_utils.database_exists')
    def test_init(self, mock_database_exists, mock_read_sql_table, mock_create_engine):
        # Mocks for command line arguments
        command_line_argument_parser = Mock()
        args = Mock()
        args.config = "config/database_configuration.json"
        args.csv = None
        command_line_argument_parser.read_arguments.return_value = args

        # Mock the engine creation and its url attribute
        mock_engine = Mock()
        mock_engine.url = 'sqlite:///test.db'
        mock_create_engine.return_value = mock_engine

        # Mock database_exists to return True regardless of input
        mock_database_exists.return_value = True

        # Mock the read_sql_table to return a DataFrame when called
        mock_read_sql_table.return_value = pandas.DataFrame({'column': []})

        # Instantiate the SqlDatabase object, which will trigger the setup method
        test_object = sqlDatabase.SqlDatabase(command_line_argument_parser)

        # Validate the setup
        mock_create_engine.assert_called_once()
        mock_database_exists.assert_called_once_with(mock_engine.url)
        self.assertEqual(mock_read_sql_table.call_count, 3)

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

