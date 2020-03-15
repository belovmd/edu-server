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
    # content = ("program HelloWorld;\n"
    #            "begin "
    #            "    readln()"
    #            "    writeln('Hello, world');\n"
    #            "end.\n")
    content = (
        'program Hello;\n'
        'var i, k, j, N: integer;\n'
        'begin\n'
        "write('enter num')\n"
        'readln(N);\n'
        'for i:=1 to 10 do\n'
        '  writeln(i*i);\n'
        "writeln('Current Num');\n"
        'writeln(N);\n'
        'end.\n'
    )
    with open("/tmp/tmp.pas", 'w') as fh:
        fh.write(content)
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

    grep_stdout = p.communicate(input='10'.encode())

    return JsonResponse({"data": str(grep_stdout), "value": "bla"})
