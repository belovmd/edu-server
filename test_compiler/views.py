from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import SampleForm

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    from django import forms
    from codemirror import CodeMirrorTextarea

    form = SampleForm()
    return render(request, 'task.html', {"frm": form})
