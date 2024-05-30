import os
import google.generativeai as genai
API_KEY = '7185632630:AAG2E9D7xxlYvIOG89E2NojgN68aQC5drBI'
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
    
    
