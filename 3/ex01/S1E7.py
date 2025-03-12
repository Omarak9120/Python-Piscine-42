from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """
        Initializes a Baratheon character.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """
        Not alive.
        """
        self.is_alive = False

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()


class Lannister(Character):
    """Why rob a bank when you can marry a Lannister and inherit the vault?"""

    def __init__(self, first_name, is_alive=True):
        """
        Initialize a Lannister character with the provided first name.

        Parameters:
            first_name (str): The first name of the character.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """
        Mark the character as not alive.
        """
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """
        Tyrion Lannister : I drink, and I know things ...
        """
        instance = cls(first_name)
        instance.is_alive = is_alive
        return instance

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()
