# Generated by Django 4.2.3 on 2023-10-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contacto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=30, verbose_name="Nombre")),
                ("apellido", models.CharField(max_length=30, verbose_name="Apellido")),
                ("email", models.CharField(max_length=50, verbose_name="Email")),
                ("mensaje", models.CharField(max_length=500, verbose_name="Mensaje")),
            ],
        ),
    ]