from django.db import models

# Create your models here.
class Produto(models.Model):
    id_prod = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    descricao = models.TextField(max_length=255)
    preco = models.FloatField()
    validade = models.DateField()

