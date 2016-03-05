from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializer import *
from .tables import *


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET', 'POST'])
def get_log(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        log = LogEntry.objects.all()
        serializer = LogEntrySerializer(log, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = LogEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_logentry(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        log = LogEntry.objects.get(id=id)
    except LogEntry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LogEntrySerializer(log)
        return JSONResponse(serializer.data)


def index(request):
    context = {}
    log = LogEntry.objects.all()
    context['log'] = log
    table = LogTable(LogEntry.objects.all())
    context['table'] = table
    return render(request, 'index.html', context)


def sample(request, id):
    context = {}
    try:
        sample_by_id = Sample.objects.get(id=id)
    except Sample.DoesNotExist:
        return Http404
    table = SampleTable(LogEntry.objects.filter(sample=sample_by_id))
    context['table'] = table
    return render(request, 'sample.html', context)


def drillhole(request):
    context = {}
    drillhole1 = DrillholeTable(Sample.objects.filter(drillhole=1))
    drillhole2 = DrillholeTable(Sample.objects.filter(drillhole=2))
    drillhole3 = DrillholeTable(Sample.objects.filter(drillhole=3))
    drillhole4 = DrillholeTable(Sample.objects.filter(drillhole=4))
    context['drillhole1'] = drillhole1
    context['drillhole2'] = drillhole2
    context['drillhole3'] = drillhole3
    context['drillhole4'] = drillhole4
    return render(request, 'drillhole.html', context)
