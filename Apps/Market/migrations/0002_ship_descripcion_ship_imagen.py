# Generated by Django 4.2.13 on 2024-06-23 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='descripcion',
            field=models.TextField(default='Sin descripcion'),
        ),
        migrations.AddField(
            model_name='ship',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='market'),
        ),
    ]
