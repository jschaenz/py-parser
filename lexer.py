from abc import abstractmethod, ABC


class LexType(ABC):
    """Abstract class for Objects that are generated by the Lexer"""
    @abstractmethod
    def to_str(self) -> str:
        """Printing the Objects as 'Object[Value]' for testing purposes"""
        pass

    @abstractmethod
    def get_value(self) -> str or int:
        """Returns the Value of the Object"""
        pass


class LexString(LexType):
    value: str  # stores a String

    def __init__(self, value):
        assert(isinstance(value, str))
        self.value = value

    def to_str(self):
        """method to create strings for printing to test Lexer separation of tokens"""
        return "STRING[" + self.value + "] "

    def get_value(self) -> str:
        """Getter to return the value of the String"""
        return self.value


class LexSpecial(LexType):
    value: str  # stores a String representing a Special Character

    def __init__(self, value):
        assert (isinstance(value, str))
        self.value = value

    def to_str(self):
        """method to create strings for printing to test Lexer separation of tokens"""
        return "SPECIAL[" + self.value + "] "

    def get_value(self) -> str:
        """Getter to return the value of the Special"""
        return self.value


class LexNumber(LexType):
    value: str  # stores a Number as string

    def __init__(self, value):
        assert (isinstance(value, str))
        self.value = value

    def to_str(self):
        """method to create strings for printing to test Lexer separation of tokens"""
        return "NUMBER[" + self.value + "] "

    def get_value(self) -> str:
        """Getter to return the value of the Number"""
        return self.value


class Lexer:

    @staticmethod
    def __get_type(item: str) -> str:
        """Returns the Type of Data we found for the corresponding EBNF"""
        assert (isinstance(item, str))
        assert (len(item) == 1)  # We want to look at one character at a time only

        # check if number
        if item in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            is_type = "NUMBER"
        # check if in a-z or A-Z
        elif item.isalpha():
            is_type = "STRING"
        # check if space
        elif item in (" ", "\t", "\n"):
            is_type = "IGNORE"
        else:
            is_type = "SPECIAL"
        # otherwise it gets treated as special character

        assert is_type in ("STRING", "NUMBER", "IGNORE", "SPECIAL")
        return is_type

    def lex(self, s: str) -> list:
        """ Splits the String into tokens of digits, unarys, operators or syntax elements"""
        assert(len(s) > 0)
        assert(isinstance(s, str))

        tokens = []
        buffer = ""
        for i in range(0, len(s)):
            char = s[i]
            buffer += char
            char_type = self.__get_type(char)

            if char_type in ("NUMBER", "STRING"):  # checks for continuation if number or string

                if i != len(s) - 1:  # don't check for the next one if we're at the last char of string s
                    next_char_type = self.__get_type(s[i + 1])
                    if char_type != next_char_type:
                        if char_type == "NUMBER":
                            tokens.append(LexNumber(buffer))
                        else:
                            tokens.append(LexString(buffer))
                        buffer = ""
                else:
                    if char_type == "IGNORE":
                        tokens.append(LexNumber(buffer))
                    elif char_type == "NUMBER":
                        tokens.append(LexNumber(buffer))
                    else:
                        tokens.append(LexString(buffer))
                    buffer = ""

            elif char_type == "SPECIAL":  # we append and empty the buffer for operators and parenthesis
                tokens.append(LexSpecial(buffer))
                buffer = ""
            else:  # filter out any empty spaces
                buffer = ""

        assert tokens  # Make sure there are tokens in the list

        return tokens
