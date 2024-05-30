import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(
  api_key=API_KEY
)
model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])
instruction="Respond in this way like you are explaining things in two to three with concise and use of easy word."
while(true):
  question=input("You: ")
  if(question.strip()==''):
    break
    response=chat.send_message(intruction + question)
    print('\n')
    print(f"techbire: {response.text}")
    print('\n')
    
    
