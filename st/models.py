from django.db import models
from django.utils import timezone
from geoposition.fields import GeopositionField


class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class DrillHole(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Bin(models.Model):
    tag = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)


class Lab(models.Model):
    tag = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)


class Sample(models.Model):
    drillhole = models.ForeignKey(DrillHole, on_delete=models.CASCADE)
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE, null=True, blank=True)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, null=True, blank=True)

    tag = models.CharField(max_length=200, unique=True)
    STATUS_CHOICES = [
        (1, 'somewhere'),
        (2, 'bin'),
        (3, 'lab'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    time_created = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(default=timezone.now)
    current_geo = GeopositionField(null=True)

    def __str__(self):
        return self.tag


class LogEntry(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE, null=True, blank=True)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, null=True, blank=True)

    STATUS_CHOICES = [
        (1, 'somewhere'),
        (2, 'bin'),
        (3, 'lab'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    time = models.DateTimeField(default=timezone.now)
    geo = GeopositionField(null=True)

    def __str__(self):
        return str(self.id) + ' - sample' + str(self.sample.id)
