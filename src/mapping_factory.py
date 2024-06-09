from .mapping import Mapping

class MappingFactory:
    def __init__(self):
       pass 

    def create(self, training_index, database):
        return Mapping(training_index, database)
