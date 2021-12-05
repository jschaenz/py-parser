from AST_Classes.AST import AST


class OPERATOR(AST):
    """Class that represents a mathematic operation of either multiplication, devision, addition or subtraction"""
    content: str  # Variable stores the operator for the calculation of two values

    def __init__(self, content: str):
        assert content in ("+", "-", "*", "/")  # "+" | "-" | "*" |"/" are allowed values for our known operators
        self.content = content

    def calculate(self, left, right) -> int:
        """Calculates the integers left and right by multiplication, devision, addition or subtraction"""
        assert (isinstance(left, int), isinstance(left, int))
        assert (left >= 0 and right >= 0)

        if self.content == "/":
            result = left / right
        elif self.content == "*":
            result = left * right
        elif self.content == "+":
            result = left + right
        else:
            result = left - right

        assert isinstance(result, int)
        return result
