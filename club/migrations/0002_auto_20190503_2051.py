# Generated by Django 2.2 on 2019-05-03 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logmessage',
            old_name='message',
            new_name='mensaje',
        ),
    ]