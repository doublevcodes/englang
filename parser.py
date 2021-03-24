from typing import Union
from tokens import Token
from tokens import Integer, Float

class NumberNode:
    """
    Node for storing numeric values
    This includes `Integer` and `Float`
    """
    def __init__(self, tok: Union[Integer, Float]) -> None:
        self.tok = tok
        return None

    def __repr__(self) -> str:
        return f"{self.tok}"

class BinaryOperationNode:
    
    def __init__(self, left_tok: Union[Integer, Float], op_tok, right_tok: Union[Integer, Float]) -> None:
        self.left_tok = left_tok
        self.op_tok = op_tok
        self.right_tok = right_tok

    def __repr__(self) -> str:
        return f'({self.left_tok}, {self.op_tok}, {self.right_tok})'

class UnaryOperationNode:

    def __init__(self, op_tok, node) -> None:
        self.op_tok = op_tok
        self.node = node

    def __repr__(self) -> str:
        return f'({self.op_tok}, {self.node})'

class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.token_idx = -1
        self.advance()

    def advance(self):
        self.token_idx += 1
        if self.token_idx < len(self.tokens):
            self.current_tok = self.tokens[self.token_idx]
        return self.current_tok

    def parse(self):
        res = self.expr()
        return res

    def factor(self):
        res = ParseResult()
        tok: Token = self.current_tok
        if tok.type_ in ("ADDITION", "SUBTRACTION"):
            res.register(self.advance())
            factor = res.register(self.factor())
            if res.error: return res
            return res.success(UnaryOperationNode(tok, factor))
        elif tok.type_ in ("INTEGER", "FLOAT"):
            res.register(self.advance())
            return res.success(NumberNode(tok))
        elif tok.type_

        return res.failure(TypeError("Expected int or float"))

    def term(self):
        return self.binary_operation_scan(self.factor, ("MULTIPLICATION", "DIVISION"))

    def expr(self):
        return self.binary_operation_scan(self.term, ("ADDITION", "SUBTRACTION"))

    def binary_operation_scan(self, function, op_check):
        res = ParseResult()
        left = res.register(function())
        if res.error: return res
        while self.current_tok.type_ in op_check:
            operational_tok = self.current_tok
            res.register(self.advance())
            right = res.register(function())
            if res.error: return res
            left = BinaryOperationNode(left, operational_tok, right)
        return left

class ParseResult:

    def __init__(self) -> None:
        self.error = None
        self.node = None

    def register(self, res):
        if isinstance(res, Parser):
            self.error = res.error if res.error else None
            return res.node

        return res

    def success(self, node):
        self.node = node
        return self.node

    def failure(self, error):
        self.error = error
        return self.error