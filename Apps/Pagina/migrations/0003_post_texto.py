# Generated by Django 4.2.13 on 2024-06-22 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0002_post_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='texto',
            field=models.TextField(default='No hay texto para mostrar'),
        ),
    ]
