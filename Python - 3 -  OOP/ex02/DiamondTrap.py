from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """Class representing a character in the King family of Game of Thrones"""

    def __init__(self, first_name, is_alive=True):
        """Constructor for the King class"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "blue"
        self.hairs = "dark"
        self.is_alive = True

    def __str__ (self):
        """Method to return a string representation of the King class"""
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__ (self):
        """Method to return a string representation of the King class"""
        return self.__str__()

    def die(self):
        """Method to kill a King character"""
        self.is_alive = False

    def set_eyes(self, eyes):
        """Method to set the eyes of a King character"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Method to set the hairs of a King character"""
        self.hairs = hairs

    def get_eyes(self):
        """Method to get the eyes of a King character"""
        return self.eyes

    def get_hairs(self):
        """Method to get the hairs of a King character"""
        return self.hairs