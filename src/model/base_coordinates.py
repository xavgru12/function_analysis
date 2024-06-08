class BaseCoordinates:
    """Base coordinates model."""

    def __init__(
        self,
        name,
        x_y_pairs,
    ):
        """Initialize base coordinates."""
        self.x_y_pairs = x_y_pairs
        self.name = str(name)
        self.entries = len(self.x_y_pairs)
        print(self.name)


if __name__ == "__main__":
    base_coordinates = BaseCoordinates()
