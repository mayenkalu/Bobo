from django.http import JsonResponse
from chatbot.models import Message
import openai

def chatbot(request):
    if request.method == 'POST':
        user_message = request.POST['message']
        # Save the user message to the database
        Message.objects.create(user=request.user, text=user_message)
        
        # Generate chatbot response using the ChatGPT API
        response = openai.ChatCompletion.create(
            model="your-chatgpt-model-id",
            messages=[
                {"role": "system", "content": "You are a helpful and friendly chatbot."},
                {"role": "user", "content": user_message},
            ]
        )
        
        # Save the chatbot response to the database
        Message.objects.create(user=None, text=response.choices[0].message.content)
        
        return JsonResponse({'response': response.choices[0].message.content})
    else:
        return JsonResponse({'error': 'Invalid request method'})
