from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import *
from .serializer import *


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def get_log(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        log = LogEntry.objects.all()
        serializer = LogEntrySerializer(log, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LogEntrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def get_logentry(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        log = LogEntry.objects.get(id=id)
    except LogEntry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LogEntrySerializer(log)
        return JSONResponse(serializer.data)


@csrf_exempt
def add_logentry(request):
    log = LogEntry.objects.all()

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LogEntrySerializer(log, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)


def index(request):
    context = {}
    log = LogEntry.objects.all()
    context['log'] = log
    return render(request, 'index.html', context)
