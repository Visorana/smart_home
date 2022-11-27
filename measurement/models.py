from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
