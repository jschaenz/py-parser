from abc import abstractmethod, ABC


class SOLVEABLE(ABC):
    """Acts as an Interface for the classes that can solve an expression, binary operations or values"""
    @abstractmethod
    def solve(self) -> int:
        """Returns a numeric value as an integer"""
        pass
