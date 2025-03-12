class calculator:
    """Calculator for vector-scalar operations."""

    def __init__(self, vector):
        """Initialize with a vector."""
        self.vector = vector

    def __add__(self, scalar) -> None:
        """Add scalar to vector."""
        if isinstance(scalar, (int, float)):
            result = [x + scalar for x in self.vector]
            print(result)
            return result
        print("Error: Addition only supports a scalar.")

    def __mul__(self, scalar) -> None:
        """Multiply vector by scalar."""
        if isinstance(scalar, (int, float)):
            result = [x * scalar for x in self.vector]
            print(result)
            return result
        print("Error: Multiplication only supports a scalar.")

    def __sub__(self, scalar) -> None:
        """Subtract scalar from vector."""
        if isinstance(scalar, (int, float)):
            result = [x - scalar for x in self.vector]
            print(result)
            return result
        print("Error: Subtraction only supports a scalar.")

    def __truediv__(self, scalar) -> None:
        """Divide vector by scalar."""
        if not isinstance(scalar, (int, float)):
            print("Error: Division only supports a scalar.")
            return
        if scalar == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = [x / scalar for x in self.vector]
        print(result)
        return result
