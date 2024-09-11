from django.shortcuts import render
import g4f
from .models import Chats


def index(request):
    return render(request , 'index.html')


def features(request):
    return render(request , 'features.html')



def chatbot(request):
    bot_reply = None
    user_message = ""

    if request.method == "POST":
        user_message = request.POST.get('message')
        if user_message:
            # Interact with GPT using the g4f library
            response = g4f.ChatCompletion.create(
                model='gpt-4',
                messages=[{"role": "user", "content": user_message}]
            )
            bot_reply = response

        Chats.objects.create(user_chat=user_message, bot_responce=bot_reply)
            
    obj = Chats.objects.all() 
    return render(request, 'home.html', {
        'user_message': user_message,
        'bot_reply': bot_reply,
        'obj':obj,
    })