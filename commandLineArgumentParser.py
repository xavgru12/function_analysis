import argparse
import os
from typing import Optional
from typing import Any

class CommandLineArgumentParser:
    def __init__(self):
        self.args = Optional[Any]
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--csv",
            help="path to directory which contains train.csv, ideal.csv and test.csv",
            const="data",
            nargs='?',
            type=os.path.abspath,
        )
        self.args = parser.parse_args()

    def readArguments(self):
        return self.args


parser = CommandLineArgumentParser()
args = parser.readArguments()
print(args.csv)
#https://stackoverflow.com/questions/15301147/python-argparse-default-value-or-specified-value
#https://stackoverflow.com/questions/30487767/check-if-argparse-optional-argument-is-set-or-not
# class vs instance variables
# https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
