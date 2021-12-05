from AST_Classes.INTERFACE_TO_INT import TO_INT
from AST_Classes.AST import AST


class WORD(AST, TO_INT):
    """Any of 6 predefined words that represent a predefined numeric value"""
    word: str  # "one" | "two" | "three" | "eins" | "zwei" | "drei"

    words = {
        "eins": 1,
        "zwei": 2,
        "drei": 3,
        "one": 1,
        "two": 2,
        "three": 3
    }

    def __init__(self, word):  # constructor
        assert (word in self.words.keys())  # make sure the string is an allowed value
        self.word = word

    def to_int(self) -> int:
        """Returns a numeric value as an integer depending on the string"""
        number = self.words[self.word]
        assert isinstance(number, int)
        assert number > 0

        return number
