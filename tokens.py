class Position:

    def __init__(self, line = 0, column = 0):
        self.line = line
        self.column = column
        self._position = -1

    def add_column(self):
        self.column += 1

    def add_line(self):
        self.line += 1

    def _move_along(self):
        self._position += 1

class Token:

    def __init__(self, type_, content):
        self.type_ = type_
        self.content = content
        return

    def __repr__(self):
        return f"{self.type_}: {self.content}"

class Integer(Token):

    def __init__(self, int_):
        super().__init__("INTEGER", int_)

class Float(Token):

    def __init__(self, float_):
        super().__init__("FLOAT", float_)

class Addition(Token):

    def __init__(self):
        super().__init__("ADDITION", "+")

class Subtraction(Token):

    def __init__(self):
        super().__init__("SUBTRACTION", "-")

class Multiplication(Token):

    def __init__(self):
        super().__init__("MULTIPLICATION", "*")

class Division(Token):

    def __init__(self):
        super().__init__("DIVISION", "/")