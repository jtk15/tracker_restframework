from django.db import models

class State(models.Model):
    name = models.CharField('Estado', max_length=30)
    abbreviation = models.CharField('Sigla', max_length=2)
