from .baseCoordinates import BaseCoordinates

class Training(BaseCoordinates):
    """Training coordinates model."""

    def __init__(
        self, name, x_y_pairs
    ):
        self.x_y_pairs = x_y_pairs
        self.name = str(name) 
        self.entries = len(self.x_y_pairs) 
        print(self.name)
        """Initialize the training coordinates."""
       

if __name__ == "__main__":
    training = Training()
