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

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        print(validated_data['sample_tag'])

        return LogEntry.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.sample_tag = validated_data.get('sample_tag', instance.sample_tag)
        instance.save()
        return instance
