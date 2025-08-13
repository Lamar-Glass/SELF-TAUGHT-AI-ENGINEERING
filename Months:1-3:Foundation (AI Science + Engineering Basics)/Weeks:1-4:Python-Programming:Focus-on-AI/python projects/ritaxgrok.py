import os
from openai import OpenAI  # Use the OpenAI SDK interface

QUIT_WORD = "stopgrok"  # Your custom quit word

class GrokAI:
    def __init__(self):
        self.name = "Grok"
        self.system_prompt = (
            f"You are {self.name}, a friendly, supportive AI chatbot. "
            "Respond warmly and conversationally."
        )
        self.client = OpenAI(
            api_key=os.environ.get("XAI_API_KEY"),       # Your xAI/Grok API key
            base_url="https://api.x.ai/v1"               # Endpoint for xAI's API
        )

    def chat(self, user_input):
        response = self.client.chat.completions.create(
            model="grok-4",  # Or "grok-3", "grok-3-mini", depending on access
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7
        )
        return response.choices[0].message["content"]

def main():
    grok = GrokAI()
    print(f"{grok.name}: Hello! I'm {grok.name}. How can I help you today?")
    print(f"(Type '{QUIT_WORD}' anytime to quit)")

    while True:
        user_message = input("You: ")
        if user_message.lower().strip() == QUIT_WORD:
            print(f"{grok.name}: Goodbye! Exiting now.")
            break
        reply = grok.chat(user_message)
        print(f"{grok.name}: {reply}")

if __name__ == "__main__":
    main()
