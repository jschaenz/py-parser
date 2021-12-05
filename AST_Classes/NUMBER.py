from AST_Classes.AST import AST
from AST_Classes.INTERFACE_TO_INT import TO_INT
from AST_Classes.DIGIT import DIGIT
from AST_Classes.DIGIT_WOZ import DIGIT_WOZ


class NUMBER(AST, TO_INT):
    """Class that stores a number by having a digit that is not 0 at the start
    that can be followed by digits from 0-9"""
    digits: list  # digits from 0 to 9 for digit index > 0, is a list of objects DIGIT
    digits_woz: DIGIT_WOZ  # digits from 1 to 9 for the first digit if the number

    def __init__(self, d, woz):  # constructor
        self.DIGIT = d
        self.DIGIT_WOZ = woz

    def to_int(self) -> int:
        """Returns a numeric value as an integer"""
        assert self.DIGIT_WOZ

        output = str(self.DIGIT_WOZ.get_value())
        for woz in self.DIGIT:
            output += str(woz.get_value())
        number = int(output)
        assert number > 0

        return number
