import unittest

import sqlDatabase

class TestSqlDatabase(unittest.TestCase):
    def test_init(self):
        test_object = sqlDatabase.SqlDatabase()
        
