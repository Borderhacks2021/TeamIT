from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.base import Model


class Program(models.Model):
    program_id = models.CharField(max_length=10, primary_key=True)
    program_name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"{self.program_id} - {self.program_name}"
 

class MBTISummary(models.Model):
    type = models.CharField(max_length=10, null=False)
    summary = models.TextField(null=False)

    def __str__(self):
        return self.type


class TemparementSummary(models.Model):
    type = models.CharField(max_length=30, null=False)
    summary = models.TextField(null=False)

    def __str__(self):
        return self.type

class WorkingGenius(models.Model):
    input = models.CharField(max_length=1)
    genius = models.CharField(max_length=15)
    definition = models.CharField(max_length=255)
    category = models.CharField(max_length=30)
    type = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.input} - {self.genius}"


