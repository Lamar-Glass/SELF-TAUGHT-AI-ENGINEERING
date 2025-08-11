# rita_ai_chatbot_quit.py

import openai

# Set your API key (or use an environment variable)
openai.api_key = "YOUR_OPENAI_API_KEY"

QUIT_WORD = "stoprita"  # The special quit word

class RitaAI:
    def __init__(self):
        self.name = "Rita"
        self.system_prompt = (
            f"You are {self.name}, a friendly, supportive AI chatbot. "
            "You always respond in a warm, conversational way."
        )

    def chat(self, user_input):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7
        )
        return response.choices[0].message["content"]

def main():
    rita = RitaAI()
    print(f"{rita.name}: Hello! I'm {rita.name}. How can I help you today?")
    print(f"(Type '{QUIT_WORD}' anytime to quit)")

    while True:
        user_message = input("You: ")

        if user_message.lower().strip() == QUIT_WORD:
            print(f"{rita.name}: Goodbye! Exiting now.")
            break

        reply = rita.chat(user_message)
        print(f"{rita.name}: {reply}")

if __name__ == "__main__":
    main()
