from .database import Database


class DatabaseFactory:
    """Database Factory."""

    def create(self):
        """Create Database."""
        return Database()

