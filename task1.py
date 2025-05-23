import datetime

def chatbot():
    print("Hi! I'm a chatbot. Type 'exit' to quit.")
    while True:
        user_input = input("You: ").lower().strip()
        if user_input == 'exit':
            print("Chatbot: Bye!")
            break
        elif user_input in ['hi', 'hello']:
            print("Chatbot: Hey there!")
        elif 'weather' in user_input:
            print("Chatbot: It's always sunny here!")
        elif 'time' in user_input:
            print(f"Chatbot: It's {datetime.datetime.now().strftime('%H:%M:%S')}.")
        elif 'how are you' in user_input:
            print("Chatbot: I'm good, thanks!")
        else:
            print("Chatbot: Not sure what you mean. Try 'hi', 'time', or 'weather'.")

if __name__ == "__main__":
    chatbot()
         