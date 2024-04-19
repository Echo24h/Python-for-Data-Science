from S1E9 import Character

class Baratheon(Character):
    """Class representing a character in the Baratheon family of Game of Thrones"""

    def __init__(self, first_name, is_alive=True):
        """Constructor for the Baratheon class"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Method to kill a Baratheon character"""
        self.is_alive = False

    def __str__ (self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__ (self):
        return self.__str__()


class Lannister(Character):
    """Class representing a character in the Lannister family of Game of Thrones"""

    def __init__(self, first_name, is_alive=True):
        """Constructor for the Lannister class"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Method to kill a Lannister character"""
        self.is_alive = False

    def create_lannister(self, is_alive=True):
        """Method to create a Lannister character"""
        return Lannister("Tyrion", is_alive)

    def __str__ (self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__ (self):
        return self.__str__()


if __name__ == "__main__":
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")