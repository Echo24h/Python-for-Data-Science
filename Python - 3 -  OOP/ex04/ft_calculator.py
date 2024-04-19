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

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Method to calculate the dot product of two vectors"""
        dot_product = sum([x * y for x, y in zip(V1, V2)])
        print("Dot Product is:", dot_product)

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Method to add two vectors"""
        sum_vec = [x + y for x, y in zip(V1, V2)]
        print("Add Vector is:", sum_vec)

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Method to subtract two vectors"""
        sub_vec = [x - y for x, y in zip(V1, V2)]
        print("Sous Vector is:", sub_vec)


if __name__ == "__main__":
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)
