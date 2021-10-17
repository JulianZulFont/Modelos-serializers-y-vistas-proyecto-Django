from django.db import models


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    prod_precio = models.IntegerField(default=0)
    prod_referencia = models.CharField(max_length=45)
    prod_descripcion = models.TextField ('Descripción', unique=False,default='null')
    prod_categoria = models.CharField('Categoria', max_length = 40, unique=False,default='null')


