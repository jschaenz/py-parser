from AST_Classes.AST import AST


class DIGIT_WOZ(AST):
    """Object that represents an Number from 1-9"""
    digit: int  # int of value 1-9

    def __init__(self, digit):  # constructor
        assert (1 <= digit <= 9)
        self.digit = digit

    def get_value(self):
        return self.digit
