from __future__ import unicode_literals
from django.db import models

class Busca(models.Model):
    palavra = models.CharField(max_length=15)
    datainicio = models.DateTimeField
    datafim = models.DateTimeField

    def __str__(self):
        return self.palavra
