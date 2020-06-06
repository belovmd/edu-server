from subprocess import Popen, PIPE, STDOUT

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from . import models


@ensure_csrf_cookie
@login_required
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    tasks = models.Task.objects.all()
    return render(request, 'menu.html', {'tasks': tasks})


@ensure_csrf_cookie
@login_required
def task_view(request, slug):
    task = get_object_or_404(models.Task, slug=slug)
    tasks = models.Task.objects.filter(class_id=task.class_id,
                                       paragraph=task.paragraph)

    lesson_tasks = tasks.filter(class_homework='lesson').order_by('task_number').all()
    hw_tasks = tasks.filter(class_homework='homework').order_by('task_number').all()
    paragraph = get_object_or_404(models.Paragraph,
                                  paragraph_id=task.paragraph,
                                  class_id=task.class_id)

    return render(request, 'task.html', {'lesson_tasks': lesson_tasks,
                                         'hw_tasks': hw_tasks,
                                         'task': task,
                                         'paragraph': paragraph})


@login_required
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


def _modify_lesson_tasks(lesson_tasks):
    result_tasks = []
    for task in lesson_tasks:
        populated_task = {'task_title': task.task_title,
                          'task': task}
        if task.task_number[task.task_number.find('.')+1] == '0':
            populated_task['task_number'] = (task.task_number[:task.task_number.find('.')+1]+
                                             task.task_number[task.task_number.find('.')+2])
        else:
            populated_task['task_number'] = task.task_number
        result_tasks.append(populated_task)
    return result_tasks


@login_required
def all_tasks(request, class_id, paragraph_id):
    paragraph = get_object_or_404(models.Paragraph, class_id=class_id,
                                  paragraph_id=paragraph_id)
    paragraphs = models.Paragraph.objects.filter(class_id=paragraph.class_id)
    tasks = models.Task.objects.filter(paragraph=paragraph_id)

    lesson_tasks = tasks.filter(class_homework='lesson').order_by('task_number').all()
    hw_tasks = tasks.filter(class_homework='homework').order_by('task_number').all()
    populated_lesson = _modify_lesson_tasks(lesson_tasks)
    return render(request, 'all_tasks.html', {'lesson_tasks': populated_lesson,
                                              # 'populated_lessons': populated_lesson,
                                              'hw_tasks': hw_tasks,
                                              'paragraph': paragraph,
                                              'paragraphs': paragraphs})


@login_required
def all_paragraphs(request, class_id):
    classes = [par.class_id for par in models.Paragraph.objects.distinct('class_id').all()]

    paragraphs = models.Paragraph.objects.filter(class_id=class_id).all()
    return render(request, 'all_paragraphs.html', {'class_': class_id,
                                                   'paragraphs': paragraphs,
                                                   'classes': classes})


def program(request):
    classes = [par.class_id for par in models.Paragraph.objects.distinct('class_id').all()]

    return render(request, 'program.html', {'classes': classes})
