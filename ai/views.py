from django.shortcuts import render
import g4f

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
            

    return render(request, 'home.html', {
        'user_message': user_message,
        'bot_reply': bot_reply,
    })