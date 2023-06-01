from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class cadastro_of(models.Model):
    criador = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    numero_da_of = models.CharField(max_length=8)
    codigo_produto = models.CharField(max_length=5)
    produto = models.TextField()
    quantidade_of = models.IntegerField()

    def __str__(self) -> str:
        return self.numero_da_of
    