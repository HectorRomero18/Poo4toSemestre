from django.urls import path
from .views import chatbot_api, index


app_name = 'chatbot'
urlpatterns = [
    # Define the URL for the chatbot API
    path('', index, name='index'),
    path('api/', chatbot_api, name='api'),
    
]
