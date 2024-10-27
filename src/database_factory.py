from .database import Database


class DatabaseFactory:
    def __init__(self):
        pass

    def create(self):
        return Database()
