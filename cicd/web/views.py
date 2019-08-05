import os

from django.http import HttpResponse


def index(request):
    pod_name = os.environ.get('POD_NAME')
    app_version = os.environ.get('APP_VERSION')
    return HttpResponse("%s: Hello, world. This is version %s" %(pod_name, app_version))