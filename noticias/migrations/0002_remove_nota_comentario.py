# Generated by Django 2.2.1 on 2019-05-07 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nota',
            name='comentario',
        ),
    ]