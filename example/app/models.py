from django.db import models


class Person(models.Model):
    name = models.CharField(verbose_name="full name", max_length=100)
