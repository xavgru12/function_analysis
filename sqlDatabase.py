import argparse 
import os
import commandLineArgumentParser
from typing import Optional
from typing import Any

class SqlDatabase:
    def __init__(self):
        self.command_line_argument_parser = commandLineArgumentParser.CommandLineArgumentParser()
        arguments = self.command_line_argument_parser.readArguments() 
        if arguments.csv:
           self.write_csv(arguments.csv) 




    def setup(self):
        pass

    def write_mapping(self):
        return None 

    def write_csv(self, path):
        train = os.path.join(path, "train.csv")
        if not os.path.isfile(train):
            raise FileNotFoundError(train) 

        ideal = os.path.join(path, "ideal.csv")
        if not os.path.isfile(ideal):
            raise FileNotFoundError(ideal) 

        test = os.path.join(path, "test.csv")
        if not  os.path.isfile(test):
            raise FileNotFoundError(test)


    def write(self):
        # write to sql
        pass

    def read(self):
        pass


sql_database = SqlDatabase()
#args = parser.readArguments()
#print(args.csv)

