# Generated by Django 4.2.13 on 2024-06-22 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pagina', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='post'),
        ),
    ]
