from AST_Classes.AST import AST
from AST_Classes.INTERFACE_TO_INT import TO_INT


class UNARY(AST, TO_INT):
    """Represents an unary, that uses the amount of sequential chars '|' to represent a numeric value"""

    UNARY: str  # Variable stores the unary "|" with all subsequent "|"'s

    def __init__(self,un):  # constructor
        assert ("".join(set(un)) == "|")  # makes sure the value only consists of char "|"
        self.UNARY = un

    def to_int(self) -> int:
        """Returns a numeric value as an integer, depending on the amount of sequential char '|' """
        length = len(self.UNARY)
        assert length

        return length
