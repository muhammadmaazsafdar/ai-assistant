from groq import Groq

from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

chat_history = [
    {"role":"system","content":"You are an AI Assistant that has to do jobs of multiple person at once.You are always respectful to customers calling and will be handling their queries with utmost care"}
]

print("AI Assistant is ready! Type 'quit' to exit.\n")

while True:
    user_input = input("Human: ")

    if user_input.lower() == "quit":
        print("Stay blessed")
        break


    chat_history.append({"role":"user","content": user_input})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=chat_history
    )

    reply = response.choices[0].message.content
    chat_history.append({"role":"assistant","content":reply})
    print (f"Assistant: {reply}")
