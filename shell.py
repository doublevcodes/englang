import sys
from lexing.lexer import Lexer
from parsing.parser import Parser


def shell(fn, text):
    # Generate tokens
    lexer = Lexer(fn, text)
    tokens, exception = lexer.make_tokens()
    if exception:
        return None, exception

    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()

    return ast.node, ast.error


while True:
    input_ = input('Englang: ')
    if text == "exit()":
        sys.exit(0)
    result, error = shell('<stdin>', input_)
    if error:
        print(error.as_string())
    else:
        print(result)
