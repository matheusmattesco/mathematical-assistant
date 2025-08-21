import time
from config import generator
from math_basic import is_math_question, text_to_math_expr
from math_complex import is_complex_math, calc_sympy

def smart_chat(user_input, max_tokens=50):
    print("Gemma: pensando...", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

    # Matemática complexa
    if is_complex_math(user_input):
        result = calc_sympy(user_input)
        if result is not None:
            return f"[Calculadora Complexa] {result}"
        else:
            return "[Calculadora Complexa] Erro ao calcular a expressão."

    # Matemática básica
    elif is_math_question(user_input):
        expr = text_to_math_expr(user_input)
        try:
            result = eval(expr, {"__builtins__": None}, {})
            return f"[Calculadora] {result}"
        except Exception:
            return "[Calculadora] Erro ao calcular a expressão."

    # IA
    else:
        response = generator(user_input, max_new_tokens=max_tokens, temperature=0.3, top_p=0.8)
        return f"[IA] {response[0]['generated_text']}"
