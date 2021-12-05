from AST_Classes.AST import AST
from AST_Classes.BINARY_OP import BINARY_OP
from AST_Classes.DIGIT_WOZ import DIGIT_WOZ
from AST_Classes.DIGIT import DIGIT
from AST_Classes.EXPRESSION import EXPRESSION
from AST_Classes.NUMBER import NUMBER
from AST_Classes.OPERATOR import OPERATOR
from AST_Classes.UNARY import UNARY
from AST_Classes.VALUE import VALUE
from AST_Classes.WORD import WORD


class Parser:
    def __init__(self):  # constructor
        pass

    def parse(self, ts):  # parses tokens ts into a Tree
        if list(ts).count:
            ast = AST()
            #parse ts

            ast.print()
            rval = ast
        else:  # nothing in it
            rval = 0
        return rval

    def CREATE_BINARY_OP(self, ex1, op, ex2):
        B = BINARY_OP(ex1, op, ex2)
        return B

    def CREATE_DIGIT_WOZ(self, c):
        D = DIGIT_WOZ(c)
        return D

    def CREATE_DIGIT(self, c):
        D = DIGIT(c)
        return D

    def CREATE_EXPRESSION(self, exp, bina, v):
        E = EXPRESSION(exp, bina, v)
        return E

    def CREATE_NUMBER(self, d, woz):
        N = NUMBER(d, woz)
        return N

    def CREATE_OPERATOR(self, c):
        O = OPERATOR(c)
        return O

    def CREATE_UNARY(self, un,c):
        U = UNARY(un,c)
        return U

    def CREATE_VALUE(self,c):
        V = VALUE(c)
        return V

    def CREATE_WORD(self, c):
        W = WORD(c)
        return W

"""
                            EXPRESSION
                BINARY_OP                   VALUE
    OPERATOR                                NUMBER              UNARY             WORD
                                    DIGIT_WOZ    DIGIT      
                                                DIGIT_WOZ
"""