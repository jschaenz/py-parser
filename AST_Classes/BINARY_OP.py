from AST_Classes.AST import AST
from AST_Classes.INTERFACE_SOLVEABLE import SOLVEABLE


class BINARY_OP(AST, SOLVEABLE):
    """Represents a binary operation on two expressions that are connected with
    an operator with format: EXPRESSION, OPERATOR, EXPRESSION"""
    def __init__(self,ex1,op,ex2):  # constructor
        self.EXPRESSION1 = ex1
        self.OPERATOR = op
        self.EXPRESSION2 = ex2

    def solve(self):
        self.OPERATOR.calculate(self.EXPRESSION1.solve(), self.EXPRESSION2.solve())
