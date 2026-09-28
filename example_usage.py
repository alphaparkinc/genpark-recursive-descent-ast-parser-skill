from client import ASTParser

def main():
    tokens = [
        {"type": "NUMBER", "value": "10"},
        {"type": "PLUS", "value": "+"},
        {"type": "NUMBER", "value": "2"},
        {"type": "MUL", "value": "*"},
        {"type": "NUMBER", "value": "5"}
    ]
    parser = ASTParser(tokens)
    ast = parser.parse_expr()
    print("Recursive Descent AST Parser Verification:")
    print(f"Root AST Type: {ast['type']}, Op: {ast['op']}")
    print(f"Right Term Op: {ast['right']['op']}")

if __name__ == "__main__":
    main()
