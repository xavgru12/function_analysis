import unittest
from unittest.mock import Mock, patch
import pandas

import sqlDatabase

class TestSqlDatabase(unittest.TestCase):
    @patch('sqlalchemy.create_engine')
    @patch('sqlDatabase.pandas.read_sql_table')
    @patch('sqlDatabase.sqlalchemy_utils.database_exists')
    def test_init_read(self, mock_database_exists, mock_read_sql_table, mock_create_engine):
        command_line_argument_parser = Mock()
        args = Mock()
        args.config = "config/database_configuration.json"
        args.csv = None
        command_line_argument_parser.read_arguments.return_value = args

        mock_engine = Mock()
        mock_engine.url = 'sqlite:///test.db'
        mock_create_engine.return_value = mock_engine

        mock_database_exists.return_value = True

        mock_read_sql_table.return_value = pandas.DataFrame({'column': []})

        test_object = sqlDatabase.SqlDatabase(command_line_argument_parser)

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

