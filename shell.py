import sys
from lexing.lexer import Lexer
from parsing.parser import Parser


def run(fn, text):
    # Generate tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error

    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()

    return ast.node, ast.error


while True:
    text = input('basic > ')
    if text == "exit()":
        sys.exit(0)
    result, error = run('<stdin>', text)
    if error:
        print(error.as_string())
    else:
        print(result)
