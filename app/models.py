from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


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

