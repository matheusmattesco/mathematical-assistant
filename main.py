from transformers import pipeline
from dotenv import load_dotenv
import os
import re
import time


load_dotenv()
hf_token = os.getenv("HF_TOKEN")
if not hf_token:
    raise ValueError("Token Hugging Face não encontrado no .env")
os.environ["HUGGINGFACE_HUB_TOKEN"] = hf_token

generator = pipeline(
    "text-generation",
    model="google/gemma-2b-it"
)

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

def smart_chat(user_input, max_tokens=50):
    print("Gemma: pensando...", end="", flush=True)
    for _ in range(3):  
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

    if is_math_question(user_input):
        expr = text_to_math_expr(user_input)
        try:
            result = eval(expr, {"__builtins__": None}, {})
            return f"[Calculadora] {result}"
        except Exception:
            return "[Calculadora] Erro ao calcular a expressão."
    else:
        response = generator(user_input, max_new_tokens=max_tokens, temperature=0.3, top_p=0.8)
        return f"[IA] {response[0]['generated_text']}"


if __name__ == "__main__":
    print("Chat Gemma (digite 'sair' para encerrar)")
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Saindo do chat...")
            break
        response = smart_chat(user_input)
        print(response)
