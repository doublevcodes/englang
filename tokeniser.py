
from tokens import Position
from tokens import Integer
from tokens import Float
from tokens import Addition
from tokens import Subtraction
from tokens import Multiplication
from tokens import Division
from tokens import LeftParenthesis
from tokens import RightParenthesis
from tokens import String
from tokens import EOFToken

from errors import UnexpectedEndOfFile

# Break up the code into an array of characters
code = [char for char in "2 + 2 * 2 / 2"]


class Tokeniser:

    def __init__(self):
        self.code = code
        self.position = Position()
        self.tokens = []
        self.current_char = None
        self.advance()
    
    def advance(self) -> None:
        """
        Moves the `current_char` of the `code` along one character
        """
        self.position._move_along()
        self.current_char = self.code[self.position._position] if self.position._position < len(self.code) else None
        return None
    
    def _tokenise(self):
        """
        Returns a `list` of subclasses of `token`
        """
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
            elif self.current_char == '(':
                self.tokens.append(LeftParenthesis())
            elif self.current_char == ')':
                self.tokens.append(RightParenthesis())
            elif self.current_char in '0123456789':
                self.tokens.append(self._scan_int())
            elif self.current_char in '\"\'':
                self.tokens.append(self._scan_string(self.current_char))
            self.advance()
        self.tokens.append(EOFToken())
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

    def _scan_string(self, delim):
        string_cache = ''
        self.advance()
        while self.current_char != None and self.current_char != delim:
            string_cache += self.current_char
            self.advance()
        else:
            if self.current_char == delim:
                return String(string_cache)
            elif self.current_char == None:
                raise UnexpectedEndOfFile



