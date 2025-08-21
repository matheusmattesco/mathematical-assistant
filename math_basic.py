import re

math_words = {
    "vezes": "*",
    "x": "*",
    "mult": "*",
    "mais": "+",
    "menos": "-",
    "dividido": "/",
    "sobre": "/",
    "raiz": "**0.5",
    "quadrado": "**2",
    "cubo": "**3",
}

def is_math_question(text):
    has_number = bool(re.search(r"\d+", text))
    has_math_word = any(word in text.lower() for word in math_words)
    return has_number and has_math_word

def text_to_math_expr(text):
    expr = text.lower()
    for word, op in math_words.items():
        expr = expr.replace(word, op)
    expr = re.sub(r"[^0-9\+\-\*/\.\(\)\^]", "", expr)
    expr = expr.replace("^", "**")
    return expr
