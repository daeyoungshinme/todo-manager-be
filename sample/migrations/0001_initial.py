# Generated by Django 4.1.7 on 2023-03-28 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TodoManagerUser",
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
                ("id_user", models.CharField(max_length=20)),
                ("nm_user", models.CharField(max_length=20)),
                ("email_user", models.CharField(max_length=30)),
                ("cell_number", models.CharField(max_length=15)),
                ("dt_created", models.DateTimeField(auto_now_add=True)),
                ("dt_updated", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
