import openai
from dotenv import load_dotenv
import os
from chatbot.persona import doctor_persona

load_dotenv()  # Load environment variables from .env file

class Chatbot:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def generate_response(self, user_input):
        messages = [doctor_persona, {"role": "user", "content": user_input}]
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
        )
        reply = response.choices[0].message['content']
        return reply
