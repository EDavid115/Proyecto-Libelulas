from django.db import models

# Create your models here.

class Registrado(models.Model):
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=50)
	codigo = models.CharField(max_length=60)
	correo = models.CharField(max_length=30)

	class Meta:
		ordering = ["nombre"]
		#verbose_name_plural = "Editores"

	def __str__(self): # __unicode__ en Python 2
		#return self.nombre
		return '%s %s' % (self.nombre, self.codigo)
