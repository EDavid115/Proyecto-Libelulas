from django.db import models

# Create your models here.

# class Editor(models.Model):
# 	nombre = models.CharField(max_length=30)
# 	domicilio = models.CharField(max_length=50)
# 	ciudad = models.CharField(max_length=60)
# 	estado = models.CharField(max_length=30)
# 	pais = models.CharField(max_length=50)
# 	website = models.URLField()

# 	class Meta:
# 		ordering = ["nombre"]
# 		verbose_name_plural = "Editores"

# 	def __str__(self): # __unicode__ en Python 2
# 		return self.nombre
# 		#return '%s %s' % (self.nombre, self.pais)