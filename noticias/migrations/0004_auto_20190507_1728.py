# Generated by Django 2.2.1 on 2019-05-07 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_auto_20190507_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='slug',
            field=models.SlugField(default='#', editable=False, max_length=225),
        ),
    ]