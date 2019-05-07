from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify

class Nota(models.Model):
    titulo = models.CharField(max_length=100)
    copete = models.CharField(max_length=200)
    texto = models.TextField()
    fecha = models.DateTimeField()
    autor = models.ForeignKey('Periodista', on_delete=models.CASCADE)
    comentario = GenericRelation('Comentario')
    slug = models.SlugField(unique=False, max_length=225, default="#", editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Nota, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.titulo}"

class Periodista(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    apodo = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="noticias")
    slug = models.SlugField(unique=False, max_length=225, default="#")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.apellido + "-" + self.nombre)
        super(Periodista, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Comentario(models.Model):
    usuario = models.CharField(max_length=50)
    texto = models.TextField()

    def __str__(self):
        return f"{self.texto}"
