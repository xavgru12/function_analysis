import argparse 
import os
import commandLineArgumentParser
from typing import Optional
from typing import Any
import pandas

class SqlDatabase:
    def __init__(self):
        self.train_dataframe = Optional[Any]
        self.ideal_dataframe = Optional[Any]
        self.test_dataframe = Optional[Any]
        self.command_line_argument_parser = commandLineArgumentParser.CommandLineArgumentParser()
        arguments = self.command_line_argument_parser.readArguments() 
        if arguments.csv:
           self.write_csv(arguments.csv) 




    def setup(self):
        pass

    def write_mapping(self):
        return None 

    def write_csv(self, path):
        train_csv = os.path.join(path, "train.csv")
        if not os.path.isfile(train_csv):
            raise FileNotFoundError(train_csv) 

        ideal_csv = os.path.join(path, "ideal.csv")
        if not os.path.isfile(ideal_csv):
            raise FileNotFoundError(ideal_csv) 

        test_csv = os.path.join(path, "test.csv")
        if not os.path.isfile(test_csv):
            raise FileNotFoundError(test_csv)


        with open(train_csv, 'r') as file:
            self.train_dataframe = pandas.read_csv(file, sep=',', encoding="UTF-8")
            print(f"train:\n {self.train_dataframe}")

        with open(ideal_csv, 'r') as file:
            self.ideal_dataframe = pandas.read_csv(file, sep=',', encoding="UTF-8")
            print(f"ideal:\n {self.ideal_dataframe}")
         
        with open(test_csv, 'r') as file:
            self.test_dataframe = pandas.read_csv(file, sep=',', encoding="UTF-8")
            print(f"test:\n {self.test_dataframe}")



    def write(self):
        # write to sql
        pass

    def read(self):
        pass


sql_database = SqlDatabase()
#args = parser.readArguments()
#print(args.csv)

