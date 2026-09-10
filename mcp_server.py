import sys
import json
from client import PrattParser

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "parse":
            tokens = [tuple(t) for t in params.get("tokens", [])]
            parser = PrattParser(tokens)
            ast = parser.parse_expr()
            res = {"ast": ast}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
