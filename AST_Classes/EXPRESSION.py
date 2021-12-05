from AST_Classes.AST import AST
from AST_Classes.INTERFACE_SOLVEABLE import SOLVEABLE

class EXPRESSION(AST, SOLVEABLE):
    """An expressions content is either another expression,
    a binary operation (of two expressions) or a value"""

    def __init__(self, content):  # constructor
        self.content = content  # EXPRESSION or BINARY_OP or VALUE

    def solve(self):
        """recursively solves the expression and returns the result as an integer"""
        result = self.content.solve()
        assert result != -1

        return result
