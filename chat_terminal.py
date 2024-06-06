# chat_terminal.py
from chatbot.chatbot import Chatbot
from rich.console import Console
from rich.text import Text
import time

def main():
    chatbot = Chatbot()
    console = Console()
    
    console.print("Welcome to the Doctor Chatbot. Type 'exit' to end the conversation.", style="bold green")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            console.print("Ending the conversation. Goodbye!", style="bold red")
            break
        
        response = chatbot.generate_response(user_input)
        
        # Simulate typing animation
        typing_text = Text("Doctor is typing...", style="dim")
        console.print(typing_text)
        time.sleep(1)  # Simulating typing delay
        
        console.clear()
        console.print(f"You: {user_input}", style="bold cyan")
        console.print(f"Doctor: {response}", style="bold yellow")

if __name__ == "__main__":
    main()
