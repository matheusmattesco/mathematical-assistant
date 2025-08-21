import sympy as sp
import re

complex_math_keywords = ["integral", "derivative", "diff", "sin", "cos", "tan", "log", "sqrt", "exp"]

def is_complex_math(text):
    return any(word in text.lower() for word in complex_math_keywords)

def text_to_complex_expr(expr):
    # Substitui funções para SymPy
    expr = expr.replace("sqrt", "sp.sqrt")
    expr = expr.replace("log", "sp.log")
    expr = expr.replace("sin", "sp.sin")
    expr = expr.replace("cos", "sp.cos")
    expr = expr.replace("tan", "sp.tan")
    expr = expr.replace("^", "**")
    return expr

def calc_sympy(expr):
    x = sp.symbols('x')
    expr = text_to_complex_expr(expr)
    try:
        if expr.startswith("derivative") or expr.startswith("diff"):
            inner = re.search(r"\((.*),\s*x\)", expr)
            if inner:
                f_expr = eval(inner.group(1))
                return sp.diff(f_expr, x)
        elif expr.startswith("integral"):
            inner = re.search(r"\((.*?)(?:,\s*x)?\)", expr)
            if inner:
                f_expr = eval(inner.group(1))
                if 'x' not in str(f_expr):
                    return f_expr * x
                return sp.integrate(f_expr, x)
        else:
            return eval(expr)
    except Exception as e:
        return f"Erro: {e}"
