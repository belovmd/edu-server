from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie

from subprocess import Popen, PIPE, STDOUT


@ensure_csrf_cookie
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

    with open("/tmp/tmp.pas", 'w') as fh:
        fh.write(content)
    import os
    src = '/app/.apt/usr/lib/x86_64-linux-gnu/fpc/3.0.4/ppcx64'
    dst = '/app/.apt/usr/bin/fpc'
    os.symlink(src, dst)
    p = Popen(['/app/.apt/usr/bin/ifpc-3.0.4',
               '-Fu"/app/.apt/usr/lib/x86_64-linux-gnu/fpc/3.0.4/units/x86_64-linux/rtl"',
               '/tmp/tmp.pas'],
              stdout=PIPE,
              stdin=PIPE,
              stderr=STDOUT)

    grep_stdout = p.communicate()

    return JsonResponse({"data": str(grep_stdout), "value": "bla"})
