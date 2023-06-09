import os
from django.http import JsonResponse
from chatbot.models import Message
import requests
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from django.shortcuts import render


def chatbot(request):
    if request.method == 'POST':
        user_message = request.POST['message']
        # Save the user message to the database
        Message.objects.create(user=request.user, text=user_message)

        # Get the OpenAI API key from the environment variable
        api_key = os.getenv('OPENAI_API_KEY')

        if api_key:
            # Generate chatbot response using the OpenAI API
            response = requests.post(
                'https://api.openai.com/v1/engines/davinci-codex/completions',
                headers={
                    'Authorization': f'Bearer {api_key}',
                    'Content-Type': 'application/json',
                },
                json={
                    'prompt': user_message,
                    'max_tokens': 60,
                }
            )
            # Save the chatbot response to the database
            Message.objects.create(user=None, text=response.json()['choices'][0]['text'])
            
            return JsonResponse({'response': response.json()['choices'][0]['text']})
        else:
            return JsonResponse({'error': 'OpenAI API key not found'})
    elif request.method == 'GET':
        return render(request, 'chatbot/chatbot.html')
    else:
        return JsonResponse({'error': 'Invalid request method'})