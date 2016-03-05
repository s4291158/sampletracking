from rest_framework import serializers
from django.utils import timezone
from .models import *


class LogEntrySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    sample_tag = serializers.CharField(max_length=200, required=False, allow_null=True, allow_blank=True)
    bin_tag = serializers.CharField(max_length=200, required=False, allow_null=True, allow_blank=True)
    lab_tag = serializers.CharField(max_length=200, required=False, allow_null=True, allow_blank=True)
    status = serializers.ChoiceField(choices=STATUS_CHOICES, default=1)
    time = serializers.DateTimeField(default=timezone.now)
    lat = serializers.FloatField(required=False, allow_null=True)
    lng = serializers.FloatField(required=False, allow_null=True)
