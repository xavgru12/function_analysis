import argparse
import os
from typing import Any, Optional


class CommandLineArgumentParser:
    def __init__(self):
        self.args = Optional[Any]
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--csv",
            help="path to directory which contains train.csv, ideal.csv and test.csv",
            const="data",
            nargs="?",
            type=os.path.abspath,
        )
        parser.add_argument(
            "--config",
            help="path to config file",
            default="config/database_configuration.json",
        )
        self.args = parser.parse_args()

    def read_arguments(self):
        return self.args


parser = CommandLineArgumentParser()
args = parser.read_arguments()
print(args.csv)
