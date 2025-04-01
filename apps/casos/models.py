from django.db import models

# Create your models here.
class CasoTipo(models.Model):
    codigo = models.CharField(max_length=3, blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.TextField(blank=True, null=True)
    
    class Meta:
        # ordering = ['-fecha_creacion']
        verbose_name = 'Tipo de caso'
        verbose_name_plural = 'Tipos de casos'

    def __str__(self):
        return f"{self.codigo}-{self.nombre}"
        