from .mapping_factory import MappingFactory
from .database_factory import DatabaseFactory

from bokeh.plotting import figure, output_file, show

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


    def plot(self):
        for mapping in self.mapping_list:
            self.plot_each(mapping)


    def plot_each(self, mapping):
            training_index = mapping.training_index
            training_name = self.database.train_list[training_index].name
            ideal_index = mapping.ideal_index
            ideal_name = self.database.ideal_list[ideal_index].name
            train_data_model = self.database.train_list[training_index]
            ideal_data_model = self.database.ideal_list[ideal_index]

            output_file("trainingfunction{}.html".format(training_name))
            # defining plot with title, axes and dimensions
            plot = figure(title="training function {} and matching ideal function {} ".format(training_name, ideal_name ),
                        x_axis_label ="x",
                        y_axis_label = "y",
                        width=700 , height=500)

            self.draw_graph(plot, train_data_model, "training", "darkslateblue")

            self.draw_graph(plot, ideal_data_model, "ideal", "hotpink")

            for test_map in mapping.test_map_list:
                x_y_pair = self.database.test_list[test_map.test_list_index]
                self.plot_each_test_value(plot, x_y_pair.point.x, x_y_pair.point.y)
            show(plot)

    def draw_graph(self, plot, data_model, label, color):
        x_values = list(data_model.x_y_pairs.keys())
        y_values = list(data_model.x_y_pairs.values())
        name = data_model.name

        plot.line(x_values,
                y_values,
                legend_label = "{} function {}".format(label, name),
                line_color = color,
                line_width = 2)


    def plot_each_test_value(self, plot, x, y):
        plot.circle(x, y, size = 7, color = "orangered", legend_label = "matched test values")



if __name__ == "__main__":
    function_analysis = FunctionAnalysis()
    function_analysis.setup_mapping()
    function_analysis.execute()
    function_analysis.plot()

