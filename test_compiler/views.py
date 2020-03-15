from subprocess import Popen, PIPE, STDOUT

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie

from . import models


@ensure_csrf_cookie
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    tasks = models.Task.objects.all()
    return render(request, 'menu.html', {'tasks': tasks})


@ensure_csrf_cookie
def task_view(request, slug):
    task = get_object_or_404(models.Task, slug=slug)
    tasks = models.Task.objects.all()
    return render(request, 'task.html', {'tasks': tasks, 'task': task})


def test(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    if request.method == 'POST':
        r_json = request.POST
        with open("/tmp/tmp.pas", 'w') as fh:
            fh.write(r_json['pascal_code'])
        import os
        src = '/app/.apt/usr/lib/x86_64-linux-gnu/fpc/3.0.4/ppcx64'
        dst = '/app/.apt/usr/bin/fpc'
        try:
            os.symlink(src, dst)
        except Exception:
            pass
        p = Popen(['/app/.apt/usr/bin/ifpc-3.0.4',
                   '/tmp/tmp.pas'],
                  stdout=PIPE,
                  stdin=PIPE,
                  stderr=STDOUT)

        grep_stdout, _ = p.communicate(input=r_json['input'].encode())

        return JsonResponse({"data": grep_stdout.decode(), "value": "bla"})
