import os
from django.http import JsonResponse
from chatbot.models import Message
import requests
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def chatbot(request):
    if request.method == 'POST':
        user_message = request.POST['message']
        # Save the user message to the database
        Message.objects.create(user=request.user, text=user_message)

        # Get the OpenAI API key from the environment variable
        api_key = os.getenv('OPENAI_API_KEY')

        if api_key:
            # Generate chatbot response using the OpenAI Playground API
            response = requests.post(
                'https://api.openai.com/v1/playground/chat/completions',
                headers={
                    'Authorization': f'Bearer {api_key}',
                    'Content-Type': 'application/json',
                },
                json={
                    'messages': [{'role': 'user', 'content': user_message}],
                }
            )

            # Save the chatbot response to the database
            Message.objects.create(user=None, text=response.json()['choices'][0]['message']['content'])

            return JsonResponse({'response': response.json()['choices'][0]['message']['content']})
        else:
            return JsonResponse({'error': 'OpenAI API key not found'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
