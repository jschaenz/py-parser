from abc import abstractmethod, ABC


class TO_INT(ABC):
    """Acts as an Interface for the classes that should return numeric values upon calling the to_int method"""
    @abstractmethod
    def to_int(self) -> int:
        """Returns a numeric value as an integer"""
        pass
