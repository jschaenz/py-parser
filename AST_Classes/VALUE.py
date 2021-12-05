from AST_Classes.AST import AST
from AST_Classes.NUMBER import NUMBER
from AST_Classes.UNARY import UNARY
from AST_Classes.WORD import WORD
from AST_Classes.INTERFACE_SOLVEABLE import SOLVEABLE


class VALUE(AST, SOLVEABLE):
    """Can store types that represent a numeric value and implement the interface 'ToInt' """
    value: NUMBER or UNARY or WORD  # NUMBER | UNARY | WORD -  are allowed Types

    def __init__(self, value):  # constructor
        self.value = value

    def solve(self):
        """Returns an integer regardless if type of the value is Number, Word or Unary"""
        number = self.value.to_int()
        assert number > 0

        return number
