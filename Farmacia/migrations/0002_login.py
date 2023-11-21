# Generated by Django 4.2.5 on 2023-11-20 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farmacia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
            ],
        ),
    ]