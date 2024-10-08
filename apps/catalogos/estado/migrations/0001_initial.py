# Generated by Django 4.2 on 2024-09-20 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, unique=True, verbose_name='Código')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
                ('orden', models.IntegerField(blank=True, null=True, verbose_name='Orden')),
            ],
            options={
                'verbose_name_plural': 'Estados',
            },
        ),
    ]
