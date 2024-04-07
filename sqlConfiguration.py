import json
from typing import Optional
from typing import Any

class SqlConfiguration:
    def __init__(self):
        self.drivername = Optional[Any]
        self.username = Optional[Any]
        self.password = Optional[Any]
        self.host = Optional[Any]
        self.database = Optional[Any]
        self.parse()
        self.print()

    def parse(self):
        with open("config/database_configuration.json", "r") as file: # save config file path as attribute and parameter or constructor
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

# sql_configuration = SqlConfiguration()

if __name__ == "__main__":
    config = dict()
    config["drivername"] = "postgresql"
    config["username"] = "postgres"
    config["password"] = "postgres"
    config["host"] = "localhost"
    config["database"] = "function-analysis"
    with open("config/database_configuration.json", "w+") as file:
        json.dump(config, file, indent= 4)

