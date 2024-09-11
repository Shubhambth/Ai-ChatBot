from django.urls import path
from .views import chatbot , index , features

urlpatterns = [
    path('chat/', chatbot, name='chatbot'),
    path('', index , name='index'),
    path('features/',features,name='features'),
]