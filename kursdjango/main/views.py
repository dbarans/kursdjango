from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello(request, text="django"):
    return HttpResponse(f"Hello {text}")


def custom_greetings(request, sent1, sent2):
    return HttpResponse(f"Hello {sent1} {sent2}")
