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
    tasks = models.Task.objects.filter(class_id=task.class_id,
                                       paragraph=task.paragraph)

    lesson_tasks = tasks.filter(class_homework='lesson').order_by('task_number').all()
    hw_tasks = tasks.filter(class_homework='homework').order_by('task_number').all()

    return render(request, 'task.html', {'lesson_tasks': lesson_tasks,
                                         'hw_tasks': hw_tasks,
                                         'task': task})


def test(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    if request.method == 'POST':
        r_json = request.POST
        with open("/tmp/tmp.pas", 'w', encoding='cp1251') as fh:
            # fh.write('{$codepage UTF8}\n')
            # fh.write('uses cwstring;\n')
            # # r_json['pascal_code'].replace('string;', 'UnicodeString;')
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

        grep_stdout, _ = p.communicate(input=r_json['input'].encode('cp1251'))

        return JsonResponse({"data": grep_stdout.decode('cp1251'), "value": "bla"})


def all_tasks(request, paragraph_id):
    paragraph = get_object_or_404(models.Paragraph, paragraph_id=paragraph_id)
    paragraphs = models.Paragraph.objects.filter(class_id=paragraph.class_id)
    tasks = models.Task.objects.filter(paragraph=paragraph_id)

    lesson_tasks = tasks.filter(class_homework='lesson').order_by('task_number').all()
    hw_tasks = tasks.filter(class_homework='homework').order_by('task_number').all()

    return render(request, 'all_tasks.html', {'lesson_tasks': lesson_tasks,
                                              'hw_tasks': hw_tasks,
                                              'paragraph': paragraph,
                                              'paragraphs': paragraphs})

def all_paragraphs(request, clas):
    pass