from django.db import models

class Nota(models.Model):
    titulo = models.CharField(max_length=100)
    copete = models.CharField(max_length=200)
    texto = models.TextField()
    fecha = models.DateTimeField()
    autor = models.ForeignKey('Periodista', on_delete=models.CASCADE)
    comentario = models.ForeignKey('Comentario', on_delete=models.CASCADE)

class Periodista(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    apodo = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="noticias")

class Comentario(models.Model):
    usuario = models.CharField(max_length=50)
    texto = models.TextField()
