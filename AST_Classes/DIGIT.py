from AST_Classes.AST import AST


class DIGIT(AST):
    """Object that represents an Number from 0-9"""
    digit: int  # int of value 0-9

    def __init__(self, digit):  # constructor
        assert (0 <= digit <= 9)
        self.digit = digit

    def get_value(self):
        return self.digit
