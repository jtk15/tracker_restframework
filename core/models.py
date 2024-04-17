from django.db import models


class Base(models.Model):
    name = models.CharField('Estado', max_length=30, unique=True)


class State(Base):
    abbreviation = models.CharField('Sigla', max_length=2, unique=True)


class City(Base):
    statefk = models.ForeignKey(State, related_name="cities", on_delete=models.CASCADE, null=True)