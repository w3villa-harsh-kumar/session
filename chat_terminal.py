# chat_terminal.py
from chatbot.chatbot import Chatbot
from rich.console import Console

def main():
    chatbot = Chatbot()
    console = Console()
    
    console.print("Welcome to the Doctor Chatbot. Type 'exit' to end the conversation.", style="bold green")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            console.print("Ending the conversation. Goodbye!", style="bold red")
            break
        
        with console.status("Docker is thinking...", spinner="dots"):
            response = chatbot.generate_response(user_input)
        
        console.print(f"Doctor: {response}", style="bold yellow")

if __name__ == "__main__":
    main()
