from bokeh.plotting import figure, output_file, show

from .database_factory import DatabaseFactory
from .mapping_factory import MappingFactory


class FunctionAnalysis:
    """Use Database and Mapping in order to do a function analysis."""

    def __init__(
        self,
        database_factory=None,
        mapping_factory=None,
    ):
        """Init the FunctionAnalysis."""
        if database_factory is None:
            database_factory = DatabaseFactory()
        if mapping_factory is None:
            mapping_factory = MappingFactory()

        self.database_factory = database_factory
        self.mapping_factory = mapping_factory

        self.database = self.database_factory.create()

        self.mapping_list = []

    def setup_mapping(self):
        """Create the Mapping objects."""
        for training_index in range(len(self.database.train_list)):
            mapping = self.mapping_factory.create(training_index, self.database)
            self.mapping_list.append(mapping)

    def execute(self):
        """Execute the function analysis."""
        for mapping in self.mapping_list:
            mapping.find_smallest_mean_squared_error()
            mapping.find_max_delta()
            mapping.find_matching_test_coordinates()

    def plot(self):
        """Visual output."""
        for mapping in self.mapping_list:
            self.__plot_each(mapping)

    def __plot_each(self, mapping):
        training_index = mapping.training_index
        ideal_index = mapping.ideal_index

        train_data_model = self.database.train_list[training_index]
        ideal_data_model = self.database.ideal_list[ideal_index]

        output_file(f"trainingfunction{train_data_model.name}.html")

        plot = self.__create_plot(train_data_model.name, ideal_data_model.name)

        self.__draw_graph(plot, train_data_model, "training", "darkslateblue")

        self.__draw_graph(plot, ideal_data_model, "ideal", "hotpink")

        self.__plot_test_values(plot, mapping.test_map_list)

        show(plot)

    def __create_plot(self, training_name, ideal_name):
        return figure(
            title=(
                f"training function {training_name} "
                f"and matching ideal function {ideal_name}"
            ),
            x_axis_label="x",
            y_axis_label="y",
            width=700,
            height=500,
        )

    def __draw_graph(self, plot, data_model, label, color):
        x_values = list(data_model.x_y_pairs.keys())
        y_values = list(data_model.x_y_pairs.values())
        name = data_model.name

        plot.line(
            x_values,
            y_values,
            legend_label=f"{label} function {name}",
            line_color=color,
            line_width=2,
        )

    def __plot_test_values(self, plot, test_map_list):
        for test_map in test_map_list:
            x_y_pair = self.database.test_list[test_map.test_list_index]
            self.__plot_each_test_value(plot, x_y_pair.point.x, x_y_pair.point.y)

    def __plot_each_test_value(self, plot, x, y):
        plot.scatter(
            x,
            y,
            size=7,
            color="orangered",
            legend_label="matched test values",
        )


if __name__ == "__main__":
    function_analysis = FunctionAnalysis()
    function_analysis.setup_mapping()
    function_analysis.execute()
    function_analysis.plot()
