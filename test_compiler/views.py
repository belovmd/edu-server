from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    return render(request, 'task.html')
