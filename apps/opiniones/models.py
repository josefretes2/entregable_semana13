from django.db import models
from apps.usuarios.models import Usuarios
from apps.noticias.models import Noticias


# Create your models here.

class Opinion(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    texto   = models.TextField(verbose_name='Opinion')
    fecha   = models.DateTimeField(auto_now_add=True)
    libro   = models.ForeignKey(Noticias, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto
    
    class Meta:
        ordering = ['-fecha']