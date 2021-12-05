from abc import abstractmethod, ABC


class ToInt(ABC):
    """Acts as an Interface for the classes that should return numeric values upon calling the to_int method"""
    @abstractmethod
    def to_int(self) -> int:
        """Returns a numeric value as an integer"""
        pass


class Number(ToInt):
    """Represents a numeric value as a common integer"""
    int_value: int

    def __init__(self, int_value):
        self.value = int_value

    def to_int(self) -> int:
        """Returns a numeric value as an integer"""
        return self.value


class Unary(ToInt):
    """Represents an unary, that uses the amount of sequential chars '|' to represent a numeric value"""
    str_value: str

    def __init__(self, str_value):
        assert("".join(set(str_value)) == "|")  # makes sure the value only consists of char "|"
        self.str_value = str_value

    def to_int(self) -> int:
        """Returns a numeric value as an integer, depending on the amount of sequential char '|' """
        return len(self.str_value)


class Word(ToInt):
    """Any of 6 predefined words that represent a predefined numeric value"""
    str_value: str
    dictionary = {
        "eins": 1,
        "zwei": 2,
        "drei": 3,
        "one": 1,
        "two": 2,
        "three": 3
    }

    def __init__(self, str_value):
        assert(str_value in self.dictionary.keys())  # make sure the string is an allowed value
        self.str_value = str_value

    def to_int(self) -> int:
        """Returns a numeric value as an integer depending on the string"""
        return self.dictionary[self.str_value]


class Value:
    """Can store types that represent a numeric value and implement the interface 'ToInt' """
    value: Number or Unary or Word

    def __init__(self, value):
        self.value = value

    def get_numeric_value(self):
        """Returns an integer regardless if type of the value is Number, Word or Unary"""
        return self.value.to_int()
