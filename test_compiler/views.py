from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    return render(request, 'task.html')


def test(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    content = ("program HelloWorld;\n"
               "    begin writeln('Hello, world');\n"
               "end.\n")
    return JsonResponse({"data": content, "value": "bla"})
