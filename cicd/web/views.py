import os

from django.http import HttpResponse


def index(request):
    pod_name = os.environ.get('POD_NAME')
    return HttpResponse("%s: Hello, world. This is version 1.0" % pod_name)