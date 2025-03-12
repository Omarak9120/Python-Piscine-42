from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class for characters."""

    def __new__(cls, *args, **kwargs):
        """
        Prevents direct instantiation of Character and
        prints an error message.
        """
        if cls is Character:
            print("TypeError: Can't instantiate abstract class Character "
                  "with abstract method")
            return None
        return super().__new__(cls)

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Initializes a character.

        Args:
            first_name (str): The character's first name.
            is_alive (bool): Whether the character is alive (default: True).
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Marks the character as dead."""
        pass


class Stark(Character):
    """Represents a Stark character."""

    def __init__(self, first_name, is_alive=True):
        """Initializes a Stark character."""
        super().__init__(first_name, is_alive)

    def die(self):
        """Marks the Stark character as dead."""
        self.is_alive = False
