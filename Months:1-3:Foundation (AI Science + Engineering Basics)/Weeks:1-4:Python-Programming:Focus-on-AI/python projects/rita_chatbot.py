# rita_chatbot.py

import random

class RitaChatbot:
    def __init__(self):
        self.name = "Rita"
        self.greetings = [
            "Hello there bro! How can I help you today?",
            "Hi! I'm Rita. What's on your mind?",
            "Hey! Ready to chat?",
            "Hi there! What would you like to talk about?"
        ]
        self.farewells = [
            "Goodbye! Take care.",
            "See you later!",
            "It was nice chatting with you. Bye!",
            "Bye! Come back soon."
        ]
    
    def greet(self):
        return random.choice(self.greetings)
    
    def farewell(self):
        return random.choice(self.farewells)
    
    def respond(self, user_input):
        user_input = user_input.lower()

        if "how are you" in user_input:
            return "I'm just a bunch of Python code, but I'm doing great! How about you my guy?"
        elif "your name" in user_input:
            return f"My name is {self.name}."
        elif "bye" in user_input or "goodbye" in user_input:
            return self.farewell()
        elif "help" in user_input:
            return "Sure! You can ask me about my name, how I’m doing, or just chat casually."
        else:
            return "Interesting... tell me more."

def main():
    rita = RitaChatbot()
    print(rita.greet())

    while True:
        user_message = input("You: ")
        
        reply = rita.respond(user_message)
        print(f"{rita.name}: {reply}")
        
        if "bye" in user_message.lower() or "goodbye" in user_message.lower():
            break

if __name__ == "__main__":
    main()
