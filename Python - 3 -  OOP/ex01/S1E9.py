from abc import ABC, abstractmethod


class Character(ABC):
    """Class representing a character in the Game of Thrones universe"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Constructor for the Character class"""
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(Character):
    """Class representing a character in the Stark family of Game of Thrones"""
    def __init__(self, first_name=None, is_alive=True):
        """Constructor for the Stark class"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Method to kill a Stark character"""
        self.is_alive = False


if __name__ == "__main__":
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

