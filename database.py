import os
from typing import Any, Optional

import sqlDatabase
import ideal
import training
import test

class Database:
    """Internal database."""

    def __init__(
        self, sql_database = sqlDatabase.SqlDatabase()
    ):
        self.sql_database = sql_database
        """Initialize the internal database."""
        self.train_list = list()
        self.ideal_list = list()
        self.test_list = list()
        self.read()

    def read(self):

        self.read_train_list()
        self.read_ideal_list()
        self.read_test_list()
        print(self.test_list[0].point)
        #self.train_list = self.convert_to_internal(self.sql_database.train_dataframe)

        #self.ideal_list = self.convert_to_internal(self.sql_database.ideal_dataframe)
        #self.test_list = self.convert_to_internal(self.sql_database.test_dataframe)
        # wrap this in training classes
        #for foo in self.ideal_list:
        #    for key, value in foo.items():
        #        print(f"key: {key}, value: {value}")
        #    print()
        #    print("next dict:")
        #print(len(self.ideal_list))

    def convert_to_internal(self, pandas_dataframe):
        dict_list = {
            col: {row['x']: row[col] for _, row in  pandas_dataframe.iterrows()}
            for col in  pandas_dataframe.columns if col != 'x'
        }
        return dict_list

    def read_generic_list(self, dataframe, list_to_append, model_class):
        dict_list = self.convert_to_internal(dataframe)
        for name, coordinates in dict_list.items():
            model = model_class(name, coordinates)
            list_to_append.append(model)

    def read_train_list(self):
        self.read_generic_list(self.sql_database.train_dataframe, self.train_list, training.Training)

    def read_ideal_list(self):
        self.read_generic_list(self.sql_database.ideal_dataframe, self.ideal_list, ideal.Ideal)

    def read_test_list(self):
        dict_list = self.convert_to_internal(self.sql_database.test_dataframe)
        coordinates = dict_list["y"] 
        print(coordinates)

        for x, y in coordinates.items():
            model = test.Test(x, y)
            self.test_list.append(model)

if __name__ == "__main__":
    database = Database()
