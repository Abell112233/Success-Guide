from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    nome = models.CharField(max_length=250)
    imagem = models.ImageField(upload_to='usuario/', null=True, blank=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_permission_user_set',  
        blank=True,
    )
    
    def __str__(self):
        return self.username


class Area(models.Model):
    nome = models.CharField(max_length=150)
    material = models.IntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='area/', null=True, blank=True)

    def __str__ (self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=150)
    carga_horaria = models.IntegerField()
    endereco = models.CharField(max_length=150)
    link = models.URLField()
    area = models.ForeignKey('Area', on_delete=models.CASCADE)

    def __str__ (self):
        return self.nome

