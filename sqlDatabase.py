import os
from typing import Any, Optional

import pandas
import sqlalchemy
import sqlalchemy_utils

import commandLineArgumentParser
import sqlConfiguration


class SqlDatabase:
    def __init__(self):
        self.train_dataframe = Optional[Any]
        self.ideal_dataframe = Optional[Any]
        self.test_dataframe = Optional[Any]
        self.sql_session = None
        self.engine = None
        self.meta = None
        self.command_line_argument_parser = (
            commandLineArgumentParser.CommandLineArgumentParser()
        )
        arguments = self.command_line_argument_parser.read_arguments()
        self.configuration = sqlConfiguration.SqlConfiguration(arguments.config)
        self.setup()

        if arguments.csv:
            self.write_csv(arguments.csv)
        else:
            self.read()

        self.print()

    def setup(self):
        config = self.configuration.read()
        connection_url = sqlalchemy.engine.URL.create(
            drivername=config["drivername"],
            username=config["username"],
            password=config["password"],
            host=config["host"],
            database=config["database"],
        )
        self.engine = sqlalchemy.create_engine(connection_url)
        if not sqlalchemy_utils.database_exists(self.engine.url):
            sqlalchemy_utils.create_database(self.engine.url)

        self.meta = sqlalchemy.MetaData()
        self.meta.create_all(self.engine)
        session = sqlalchemy.orm.sessionmaker(bind=self.engine)
        self.sql_session = session()

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

        with open(train_csv) as file:
            self.train_dataframe = pandas.read_csv(file, sep=",", encoding="UTF-8")

        with open(ideal_csv) as file:
            self.ideal_dataframe = pandas.read_csv(file, sep=",", encoding="UTF-8")

        with open(test_csv) as file:
            self.test_dataframe = pandas.read_csv(file, sep=",", encoding="UTF-8")

        self.write()

    def write(self):
        print("write")
        train_table_name = "train"
        self.train_dataframe.to_sql(
            train_table_name,
            con=self.engine,
            index=False,
            if_exists="replace",
        )
        train_table = sqlalchemy.Table(
            train_table_name,
            self.meta,
            autoload_with=self.engine,
        )

        ideal_table_name = "ideal"
        self.ideal_dataframe.to_sql(
            ideal_table_name,
            con=self.engine,
            index=False,
            if_exists="replace",
        )
        ideal_table = sqlalchemy.Table(
            ideal_table_name,
            self.meta,
            autoload_with=self.engine,
        )

        test_table_name = "test"
        self.test_dataframe.to_sql(
            test_table_name,
            con=self.engine,
            index=False,
            if_exists="replace",
        )
        test_table = sqlalchemy.Table(
            test_table_name,
            self.meta,
            autoload_with=self.engine,
        )

    def read(self):
        print("read")
        self.train_dataframe = pandas.read_sql_table("train", self.engine)
        self.ideal_dataframe = pandas.read_sql_table("ideal", self.engine)
        self.test_dataframe = pandas.read_sql_table("test", self.engine)

    def print(self):
        print(f"train:\n {self.train_dataframe}")
        print(f"ideal:\n {self.ideal_dataframe}")
        print(f"test:\n {self.test_dataframe}")


sql_database = SqlDatabase()
# args = parser.readArguments()
# print(args.csv)
