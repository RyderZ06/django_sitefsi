from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request): # HttpRequest
    return HttpResponse("<h1> Страница приложения staff. </h1>")

def categories(request):
    return HttpResponse("<h1> Статьи по категориям. </h1>")