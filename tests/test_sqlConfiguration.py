import unittest

import sqlConfiguration 

class TestSqlConfiguration(unittest.TestCase):
    def test_init(self):
        test_object = sqlConfiguration.SqlConfiguration("config/database_configuration.json")
        
    def test_init_exception(self):

        with self.assertRaises(Exception):
            test_object = sqlConfiguration.SqlConfiguration("non_existent")


    def test_read(self):
        test_object = sqlConfiguration.SqlConfiguration("config/database_configuration.json")
        config = test_object.read()
        self.assertEqual(test_object.drivername, config["drivername"])
        self.assertEqual(test_object.username, config["username"])
        self.assertEqual(test_object.password, config["password"])
        self.assertEqual(test_object.host, config["host"])
        self.assertEqual(test_object.database, config["database"])

