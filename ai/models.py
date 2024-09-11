from typing import Text
from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField, TimeField

class Chats(models.Model):
  user_chat = models.TextField()
  bot_responce = models.TextField()  
  date = models.DateTimeField(auto_now_add=True)

# Create your models here.
