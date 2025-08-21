from chat_utils import smart_chat

if __name__ == "__main__":
    print("Chat (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat...")
            break
        response = smart_chat(user_input)
        print(response)
