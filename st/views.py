from django.shortcuts import render

from .models import *


def index(request):
    context = {}
    log = LogEntry.objects.all()
    context['log'] = log
    return render(request, 'index.html', context)
