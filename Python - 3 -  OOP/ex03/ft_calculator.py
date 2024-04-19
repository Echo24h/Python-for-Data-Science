class calculator:
    """A class to perform basic operations on a list of numbers"""
    def __init__(self, list):
        """Constructor for the calculator class"""
        self.list = list

    def __add__(self, object) -> None:
        """Method to add a number to a list of numbers"""
        self.list = [x + object for x in self.list]
        print(self.list)

    def __sub__(self, object) -> None:
        """Method to subtract a number from a list of numbers"""
        self.list = [x - object for x in self.list]
        print(self.list)

    def __mul__(self, object) -> None:
        """Method to multiply a list of numbers by a number"""
        self.list = [x * object for x in self.list]
        print(self.list)

    def __truediv__(self, object) -> None:
        """Method to divide a list of numbers by a number"""
        self.list = [x / object for x in self.list]
        print(self.list)


if __name__ == "__main__":
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
