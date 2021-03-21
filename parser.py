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
        print("Parsing function beginning")
        res = self.final_expression()
        print("AST has been received")
        return res

    def bin_number(self):
        tok = self.current_tok
        if tok.type_ in {"INTEGER", "FLOAT"}:
            self.advance()
            return NumberNode(tok)

    def mul_div(self):
        return self.bin_op_scan(self.bin_number, ("MULTIPLICATION", "DIVISION"))

    def final_expression(self):
        return self.bin_op_scan(self.mul_div, ("ADDITION", "SUBTRACTION"))

    def bin_op_scan(self, function, operations):
        bin_op_node = ''
        left_tok = function()
        print("left_tok given as:", left_tok)
        while self.current_tok.type_ in operations:
            print("Getting BinOp token")
            op_tok = self.current_tok
            print("BinOp token given as:", op_tok)
            self.advance()
            right_tok = function()
            self.advance()
            print("right_tok given as:", right_tok)
            bin_op_node = BinaryOperationNode(left_tok, op_tok, right_tok)
            print("Binary operation node as:", bin_op_node)
        return bin_op_node
        