import json
from typing import Any, Optional


class SqlConfiguration:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.drivername = Optional[Any]
        self.username = Optional[Any]
        self.password = Optional[Any]
        self.host = Optional[Any]
        self.database = Optional[Any]
        self.parse()
        self.print()

    def parse(self):
        with open(self.config_file_path) as file:
            config = json.load(file)
            print(config)

        self.drivername = config["drivername"]
        self.username = config["username"]
        self.password = config["password"]
        self.host = config["host"]
        self.database = config["database"]

    def print(self):
        print(f"self.drivername: {self.drivername}")
        print(f"self.username: {self.username}")
        print(f"self.password: {self.password}")
        print(f"self.host: {self.host}")
        print(f"self.database: {self.database}")

    def read(self):
        return self.__dict__

