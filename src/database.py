from .model.ideal import Ideal
from .model.test import Test
from .model.training import Training
from .sql.sql_database import SqlDatabase


class Database:
    """Internal database."""

    def __init__(
        self,
        sql_database=None,
    ):
        """Initialize the internal database."""
        self.train_list = []
        self.ideal_list = []
        self.test_list = []

        if sql_database is None:
            self.sql_database = SqlDatabase()
        else:
            self.sql_database = sql_database

        self.read()

    def read(self):
        """Read from the sql database."""
        self.read_train_list()
        self.read_ideal_list()
        self.read_test_list()

    def convert_to_internal(self, pandas_dataframe):
        """Convert the sql database entries to dictionaries."""
        return {
            col: {row["x"]: row[col] for _, row in pandas_dataframe.iterrows()}
            for col in pandas_dataframe.columns
            if col != "x"
        }

    def read_generic_list(self, dataframe, list_to_append, model_class):
        """Read from the pandas dataframe and append to internal database list."""
        dict_list = self.convert_to_internal(dataframe)
        for name, coordinates in dict_list.items():
            model = model_class(name, coordinates)
            list_to_append.append(model)

    def read_train_list(self):
        """Read the train list."""
        self.read_generic_list(
            self.sql_database.train_dataframe,
            self.train_list,
            Training,
        )

    def read_ideal_list(self):
        """Read the ideal list."""
        self.read_generic_list(
            self.sql_database.ideal_dataframe,
            self.ideal_list,
            Ideal,
        )

    def read_test_list(self):
        """Read the test list."""
        dict_list = self.convert_to_internal(self.sql_database.test_dataframe)
        coordinates = dict_list["y"]

        for x, y in coordinates.items():
            model = Test(x, y)
            self.test_list.append(model)


if __name__ == "__main__":
    database = Database()
