from client import PrattParser

def main():
    print("=== Testing Pratt Operator Precedence AST Parser ===")
    tokens = [("INT", 2), ("OP", "+"), ("INT", 3), ("OP", "*"), ("INT", 4)]
    parser = PrattParser(tokens)
    ast = parser.parse_expr()
    print("Generated AST:", ast)

    assert ast["type"] == "BinaryOp" and ast["op"] == "+"
    assert ast["right"]["op"] == "*"
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
