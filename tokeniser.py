
from tokens import Position
from tokens import Integer
from tokens import Float
from tokens import Addition
from tokens import Subtraction
from tokens import Multiplication
from tokens import Division

code = [char for char in "2 + 2 * 2 / 2"]

class Tokeniser:

    def __init__(self):
        self.code = code
        self.position = Position()
        self.tokens = []
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.position._move_along()
        self.current_char = self.code[self.position._position] if self.position._position < len(self.code) else None
    
    def _tokenise(self):
        print("Beginning tokenisation")
        while self.current_char != None:
            if self.current_char in ' \t': pass
            elif self.current_char == '+':
                self.tokens.append(Addition())
            elif self.current_char == '-':
                self.tokens.append(Subtraction())
            elif self.current_char == '*':
                self.tokens.append(Multiplication())
            elif self.current_char == '/':
                self.tokens.append(Division())
            elif self.current_char in '0123456789':
                self.tokens.append(self._scan_int())
            self.advance()
        print("Finished tokenisation with tokens: ", self.tokens)
        return self.tokens

    def _scan_int(self):
        int_cache, float_ = '', False
        while self.current_char != None and self.current_char in "1234567890.":
            if self.current_char == '.':
                if float_: break
                float_ = True
                int_cache += '.'
            else:
                int_cache += self.current_char
            self.advance()

        if float_:
            return Float(float(int_cache))
        else:
            return Integer(int(int_cache))

