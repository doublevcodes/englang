from tokeniser import Tokeniser
from parser import Parser

tokeniser = Tokeniser()
tokens = tokeniser._tokenise()

parser = Parser(tokens)
ast = parser.parse()

print(ast)