class PrattParser:
    """
    Pratt Top-Down Operator Precedence Expression Parser.
    Handles binary operations and operator binding powers.
    """
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ("EOF", None)

    def consume(self):
        tok = self.peek()
        self.pos += 1
        return tok

    def parse_expr(self, rbp=0):
        tok = self.consume()
        if tok[0] == "INT":
            left = {"type": "Literal", "value": tok[1]}
        elif tok[0] == "LPAREN":
            left = self.parse_expr(0)
            self.consume()
        else:
            raise ValueError(f"Unexpected token {tok}")

        while rbp < self._get_lbp(self.peek()):
            op_tok = self.consume()
            right = self.parse_expr(self._get_lbp(op_tok))
            left = {"type": "BinaryOp", "op": op_tok[1], "left": left, "right": right}
        return left

    def _get_lbp(self, tok):
        if tok[0] == "OP":
            if tok[1] in ("+", "-"):
                return 10
            elif tok[1] in ("*", "/"):
                return 20
        return 0
