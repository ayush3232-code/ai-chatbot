import os
import json
from datetime import datetime
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set up the model with a personality
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="You are Friday, a friendly and helpful AI assistant. Keep responses clear and concise."
)

# Start chat session (this keeps conversation memory)
chat = model.start_chat(history=[])
history_log = []

print("=" * 40)
print("   🤖 Friday — AI Chatbot (Gemini)")
print("   Type 'quit' to exit")
print("=" * 40 + "\n")

while True:
    user_input = input("You: ").strip()
    
    if not user_input:
        continue
    
    if user_input.lower() == "quit":
        filename = f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, "w") as f:
            json.dump(history_log, f, indent=2)
        print(f"\n✅ Chat saved to {filename}. Goodbye!")
        break

    try:
        response = chat.send_message(user_input)
        reply = response.text
        print(f"\nAria: {reply}\n")

        history_log.append({
            "time": datetime.now().strftime("%H:%M:%S"),
            "user": user_input,
            "bot": reply
        })

    except Exception as e:
        print(f"❌ Error: {e}\n")