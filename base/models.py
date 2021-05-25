from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import JSONField


class Operation(models.Model):
    name = models.CharField(max_length=32, verbose_name='Operation Name')

    def __str__(self):
        return self.name


class Bin(models.Model):
    name = models.CharField(max_length=64, verbose_name='Bin Name')  #for example Green Bin
    latitude = models.FloatField(verbose_name='Latitude')
    longitude = models.FloatField(verbose_name='Longitude')
    address = models.TextField(verbose_name='Bin Address', blank=True, null=True)
    operations = models.ManyToManyField(Operation, through='BinOperation')

    def __str__(self):
        return self.name


class BinOperation(models.Model):
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE, verbose_name='Bin')
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE, verbose_name='Operation')
    collection_frequency = models.IntegerField(verbose_name='Collection Frequency')
    last_collection = models.DateTimeField(verbose_name='Last Collection')

    class Meta:
        indexes = [models.Index(fields=['bin'])]  #by size of table

    def __str__(self):
        return self.bin.name + ' - ' + self.operation.name

