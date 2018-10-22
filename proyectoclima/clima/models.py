
from django.db import models


class Ciudad(models.Model):

	nombre=models.CharField(max_length=25)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural='ciudades'

