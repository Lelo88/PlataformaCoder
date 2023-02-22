# Generated by Django 4.1.2 on 2022-11-10 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entregable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_de_entrega', models.DateField()),
                ('entregado', models.BooleanField()),
                ('link', models.CharField(max_length=254)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCoder.estudiante')),
            ],
        ),
    ]