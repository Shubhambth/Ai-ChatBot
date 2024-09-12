from django.shortcuts import render , redirect
import g4f
from .models import Chats
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

User = get_user_model()

def login_view(request):
    if request.method== "POST":
        username = request.POST.get("username") 
        password = request.POST.get("password") 
        if all([username,password]):
          user = authenticate(request, username=username, password=password)
          if user is not None:
              login(request, user)
              return redirect('chatbot')
    return render(request,'login_view.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        
        try:
          user = User.objects.create_user(username=username,email=email,password=password)
          user.save()
          return redirect('login')
        except:
          return render(request,'signup_view.html',{})
      
    return render(request,'signup_view.html')

def index(request):
    return render(request , 'index.html')


def features(request):
    return render(request , 'features.html')


@login_required(login_url='/login')
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

def user_logout(request):
  auth.logout(request)
  return redirect('index')
