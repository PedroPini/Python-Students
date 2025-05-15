#DOCS https://ai.google.dev/gemini-api/docs/migrate
import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown
import os
from dotenv import load_dotenv
load_dotenv()

# Step 1: Set your API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Replace with your actual API key
console = Console()
# Step 2: Choose the Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat(history=[])
# Step 3: Create a function to ask the AI
def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"
    
# Function to send a message to the chat and get a response
def chat_with_gemini():
    print("Start chatting with Gemini! (type 'exit' to stop)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        try:
            response = chat.send_message(user_input)
            # use print first 
            # print(response.text)
            md = Markdown(response.text)
            console.print(md)

        except Exception as e:
            print("Error:", e)

# Step 4: Define main in case we will import this somewhere else
if __name__ == "__main__":
    # question = input("Ask Gemini anything: ")
    # answer = ask_gemini(question)
    # print("\nGemini says:\n", answer)
    chat_with_gemini()