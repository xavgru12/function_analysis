import unittest
import os

from src.parser.command_line_argument_parser import CommandLineArgumentParser

class TestCommandLineArgumentParser(unittest.TestCase):

    def test_init_csv(self):
        test_object = CommandLineArgumentParser(["--csv"])
        self.assertEqual(test_object.args.csv , os.path.abspath("data"))

    def test_init_csv_data(self):
        test_object = CommandLineArgumentParser(["--csv", "data"])
        self.assertEqual(test_object.args.csv , os.path.abspath("data"))

    def test_init_csv_test_data(self):
        test_object = CommandLineArgumentParser(["--csv", "test_data"])
        self.assertEqual(test_object.args.csv , os.path.abspath("test_data"))

    def test_init_csv_read(self):
        test_object = CommandLineArgumentParser(["--csv"])
        arguments = test_object.read_arguments()
        self.assertEqual(arguments.csv , os.path.abspath("data"))

    def test_init_csv_data_read(self):
        test_object = CommandLineArgumentParser(["--csv", "data"])
        arguments = test_object.read_arguments()
        self.assertEqual(arguments.csv , os.path.abspath("data"))

    def test_init_csv_test_data_read(self):
        test_object = CommandLineArgumentParser(["--csv", "test_data"])
        arguments = test_object.read_arguments()
        self.assertEqual(arguments.csv , os.path.abspath("test_data"))
        
    def test_init_config_data(self):
        test_object = CommandLineArgumentParser(["--config", "config/database_configuration.json"])
        self.assertEqual(test_object.args.config , "config/database_configuration.json")

    def test_init_config_test_data(self):
        test_object = CommandLineArgumentParser(["--config", "test_config/database_configuration.json"])
        self.assertEqual(test_object.args.config , "test_config/database_configuration.json")

    def test_init_config_read(self):
        with self.assertRaises(SystemExit):
             CommandLineArgumentParser(["--config"])

    def test_init_config_data_read(self):
        test_object = CommandLineArgumentParser(["--config", "config/database_configuration.json"])
        arguments = test_object.read_arguments()
        self.assertEqual(arguments.config, "config/database_configuration.json")

    def test_init_config_test_data_read(self):
        test_object = CommandLineArgumentParser(["--config", "test_config/database_configuration.json"])
        arguments = test_object.read_arguments()
        self.assertEqual(arguments.config, "test_config/database_configuration.json")

