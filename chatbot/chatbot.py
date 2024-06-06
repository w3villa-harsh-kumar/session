import openai
from dotenv import load_dotenv
import os
from .persona import personas

load_dotenv()  # Load environment variables from .env file

class Chatbot:
    def __init__(self, persona):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.memory = [persona]

    def generate_response(self, user_input):
        self.memory.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=self.memory
        )
        reply = response.choices[0].message['content']
        self.memory.append({"role": "assistant", "content": reply})
        return reply
