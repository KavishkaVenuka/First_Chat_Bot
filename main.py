# main.py
from OpenAI import chat_with_OpenAI

def main():
    print("----Kavishka's personal bot (type 'exit' to quit)----")
    message_history = [{"role": "system", "content": "Kavishka's personal assistant"}]

    while True:
        user_input = input("Kavishka : ")
        if user_input.lower() == 'exit':
            break
        message_history.append({"role": "user", "content": user_input})

        reply = chat_with_OpenAI(message_history)
        length = len(message_history)
        print("Bot: ", reply)
        message_history.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    main()
