import re

TOKENS = [
    ("ASYNC", r"async"),  # ✅ Nieuw token voor async functies
    ("FUNCTION", r"function"),
    ("IDENTIFIER", r"[a-zA-Z_]\w*"),
    ("VARIABLE", r"\$\w+"),
    ("TYPE", r"int|string|bool"),  # ✅ Nieuw token voor types
    ("COLON", r":"),  # ✅ Nieuw token voor return types
    ("LBRACE", r"\{"),
    ("RBRACE", r"\}"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("COMMA", r","),
    ("RETURN", r"return"),
    ("NUMBER", r"\d+"),
    ("PLUS", r"\+"),
    ("SEMICOLON", r";"),
    ("WHITESPACE", r"\s+"),  # Whitespace negeren
]

def tokenize(code):
    """Verdeelt de code in tokens."""
    tokens = []
    position = 0

    while position < len(code):
        match = None
        for token_type, pattern in TOKENS:
            regex = re.compile(pattern)
            match = regex.match(code, position)
            if match:
                value = match.group(0)
                if token_type != "WHITESPACE":  # ⛔ Whitespace negeren
                    tokens.append((token_type, value))
                position += len(value)
                break
        
        if not match:
            raise SyntaxError(f"Unexpected token: {code[position]}")

    return tokens

# ✅ Testen met async en types
code = "async function add(int $a, int $b): int { return $a + $b; }"
tokens = tokenize(code)
print(tokens)
