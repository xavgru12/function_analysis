from .mapping import Mapping


class MappingFactory:
    """Mapping Factory."""

    def create(self, training_index, database):
        """Create Mapping Factory."""
        return Mapping(training_index, database)
