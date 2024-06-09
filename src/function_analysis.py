from .mapping_factory import MappingFactory
from .database_factory import DatabaseFactory

class FunctionAnalysis:
    def __init__(self, database_factory = DatabaseFactory(), mapping_factory = MappingFactory()):
        self.database_factory = database_factory
        self.mapping_factory = mapping_factory

        self.database = self.database_factory.create()

        self.mapping_list = []


    def setup_mapping(self):
        for training_index in range(len(self.database.train_list)):
            mapping = self.mapping_factory.create(training_index, self.database)
            self.mapping_list.append(mapping)


    def execute(self):
        for mapping in self.mapping_list:
            mapping.find_smallest_mean_squared_error()
            mapping.find_max_delta()
            mapping.find_matching_test_coordinates()



if __name__ == "__main__":
    function_analysis = FunctionAnalysis()
    function_analysis.setup_mapping()
    function_analysis.execute()

