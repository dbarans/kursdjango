from django.urls import path

from main.views import hello, custom_greetings

urlpatterns = [
    path('', hello, name="hello"),
    path('<text>/', hello, name="hello2"),
    path('<sent1>/<sent2>', custom_greetings, name="custom_greetings"),
]