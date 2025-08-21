import time
from config import generator
from math_basic import is_math_question, text_to_math_expr
from math_complex import is_complex_math, calc_sympy

def smart_chat(user_input, max_tokens=50):
    print("Thinking...", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

    if is_complex_math(user_input):
        result = calc_sympy(user_input)
        if result is not None:
            return f"[Complex Calculator] {result}"
        else:
            return "[Complex Calculator] Error while calculating expression."

    elif is_math_question(user_input):
        expr = text_to_math_expr(user_input)
        try:
            result = eval(expr, {"__builtins__": None}, {})
            return f"[Calculator] {result}"
        except Exception:
            return "[Calculator] Error while calculating expression."

    else:
        response = generator(user_input, max_new_tokens=max_tokens, temperature=0.3, top_p=0.8)
        return f"[IA] {response[0]['generated_text']}"
