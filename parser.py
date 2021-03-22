class NumberNode:

    def __init__(self, tok):
        self.tok = tok

    def __repr__(self):
        return f"{self.tok}"

class BinaryOperationNode:
    
    def __init__(self, left_tok, op_tok, right_tok):
        self.left_tok = left_tok
        self.op_tok = op_tok
        self.right_tok = right_tok

    def __repr__(self):
        return f'({self.left_tok}, {self.op_tok}, {self.right_tok})'
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
        tok = self.current_tok

        if tok.type_ in ("INTEGER", "FLOAT"):
            self.advance()
            return NumberNode(tok)

    def term(self):
        return self.binary_operation_scan(self.factor, ("MULTIPLICATION", "DIVISION"))

    def expr(self):
        return self.binary_operation_scan(self.term, ("ADDITION", "SUBTRACTION"))

    def binary_operation_scan(self, function, op_check):
        left = function()
        while self.current_tok.type_ in op_check:
            operational_tok = self.current_tok
            self.advance()
            right = function()
            left = BinaryOperationNode(left, operational_tok, right)

        return left