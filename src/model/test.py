from .base_coordinates import BaseCoordinates
from .point import Point


class Test(BaseCoordinates):
    """Test coordinate model."""

    def __init__(
        self,
        x_value,
        y_value,
    ):
        """Initialize the test coordinate."""
        self.point = Point(x_value, y_value)


if __name__ == "__main__":
    test = Test()
