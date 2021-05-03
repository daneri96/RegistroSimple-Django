from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    direccion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,verbose_name ="creado el")#auto guarda automaticamente la fecha de añadir
    updated_at = models.DateTimeField(auto_now=True , verbose_name = "hora")

    
