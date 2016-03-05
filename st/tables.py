import django_tables2 as tables

from st.models import *


class LogTable(tables.Table):
    time = tables.DateTimeColumn(format="d/m/y H:m")
    infoClass = tables.TemplateColumn('<a href="/sample/{{record.id}}/">View sample</a>', verbose_name='')

    class Meta:
        model = LogEntry
        fields = {"sample", "status", "time"}
        sequence = {"time", "sample", "status"}


class SampleTable(tables.Table):
    class Meta:
        model = LogEntry
        sequence = {"time", "sample", "status"}


class DrillholeTable(tables.Table):
    last_modified = tables.DateTimeColumn(format="d/m/y")
    progressImage = tables.TemplateColumn(
        '<img height=20px; width=100px; src="/static/img/progress/{{record.status}}.png"', verbose_name='')
    infoClass = tables.TemplateColumn('<a href="/sample/{{record.id}}">View sample</a>', verbose_name='')

    class Meta:
        model = Sample
        fields = ("tag", "status", "last_modified")
        sequence = ("...", "status", "infoClass", "progressImage")
