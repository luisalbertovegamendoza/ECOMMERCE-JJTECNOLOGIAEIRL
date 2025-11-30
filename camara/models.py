from django.db import models

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    detalle = models.CharField(max_length=100 , default="Valor por defecto")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen=models.ImageField(upload_to='empleado' , blank=True , null=True)
   

    def __str__(self):
        return self.nombre