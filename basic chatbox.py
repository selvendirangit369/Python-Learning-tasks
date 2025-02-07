def chatbox():
    print("Welcome to the Chatbox! Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbox: Goodbye!")
            break
        
        response = generate_response(user_input)
        print(f"Chatbox: {response}")

def generate_response(user_input):
    # Simple responses based on keywords
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but thanks for asking!"
    elif "your name" in user_input:
        return "I'm a simple chatbox created in Python."
    elif "help" in user_input:
        return "Sure! What do you need help with?"
    else:
        return "I'm not sure how to respond to that."

if __name__ == "__main__":
    chatbox()
