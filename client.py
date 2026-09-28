"""Recursive Descent Abstract Syntax Tree (AST) Parser
100% Python Standard Library.
"""

class ASTParser:
    """Recursive descent expression and statement parser."""
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, expected_type=None):
        tok = self.peek()
        if tok is None:
            return None
        if expected_type and tok["type"] != expected_type:
            raise ValueError(f"Expected {expected_type}, got {tok['type']}")
        self.pos += 1
        return tok

    def parse_factor(self):
        tok = self.consume()
        if tok["type"] == "NUMBER":
            return {"type": "Literal", "value": float(tok["value"])}
        elif tok["type"] == "IDENT":
            return {"type": "Identifier", "name": tok["value"]}
        elif tok["type"] == "LPAREN":
            node = self.parse_expr()
            self.consume("RPAREN")
            return node
        raise ValueError(f"Unexpected token {tok}")

    def parse_term(self):
        node = self.parse_factor()
        while self.peek() and self.peek()["type"] in ["MUL", "DIV"]:
            op = self.consume()["type"]
            right = self.parse_factor()
            node = {"type": "BinaryOp", "op": op, "left": node, "right": right}
        return node

    def parse_expr(self):
        node = self.parse_term()
        while self.peek() and self.peek()["type"] in ["PLUS", "MINUS"]:
            op = self.consume()["type"]
            right = self.parse_term()
            node = {"type": "BinaryOp", "op": op, "left": node, "right": right}
        return node
