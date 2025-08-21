from chat_utils import smart_chat

if __name__ == "__main__":
    print("Chat Gemma (digite 'sair' para encerrar)")
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Saindo do chat...")
            break
        response = smart_chat(user_input)
        print(response)
