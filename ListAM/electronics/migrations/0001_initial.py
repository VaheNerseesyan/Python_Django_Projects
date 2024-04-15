# Generated by Django 5.0.4 on 2024-04-15 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Computers",
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
                ("location", models.CharField(max_length=20)),
                ("price", models.PositiveIntegerField()),
                ("currency", models.CharField(max_length=5)),
                ("product_details", models.CharField(max_length=20)),
                ("condition", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="MobilePhones",
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
                ("location", models.CharField(max_length=20)),
                ("phone_model", models.CharField(max_length=20)),
                ("price", models.PositiveIntegerField()),
                ("currency", models.CharField(max_length=5)),
                ("storage_space", models.CharField(max_length=20)),
                ("color", models.CharField(max_length=20)),
                ("condition", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Notebook",
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
                ("location", models.CharField(max_length=20)),
                ("notebook_model", models.CharField(max_length=20)),
                ("price", models.PositiveIntegerField()),
                ("currency", models.CharField(max_length=5)),
                ("screen_size", models.PositiveIntegerField()),
                ("condition", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="TV",
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
                ("location", models.CharField(max_length=20)),
                ("tv_model", models.CharField(max_length=20)),
                ("price", models.PositiveIntegerField()),
                ("currency", models.CharField(max_length=5)),
                ("screen_size", models.PositiveIntegerField()),
                ("condition", models.CharField(max_length=10)),
            ],
        ),
    ]
