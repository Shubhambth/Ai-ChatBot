from django.urls import path
from .views import chatbot , index , features , login_view , register_view , user_logout

urlpatterns = [
    path('chat/', chatbot, name='chatbot'),
    path('', index , name='index'),
    path('features/',features,name='features'),
    path('login/',login_view,name='login'),
    path('register/',register_view, name='register'),
    path('logout/', user_logout, name='logout')
]