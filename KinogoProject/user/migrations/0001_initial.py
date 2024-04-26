# Generated by Django 5.0.4 on 2024-04-25 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bookmarks",
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
                ("count", models.SmallIntegerField()),
                ("film_id", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="HistoryViews",
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
                ("view_date", models.DateTimeField()),
                ("film_id", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="OneTimePassword",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=6)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("attempted_left", models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="RatedFilms",
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
                ("rate", models.SmallIntegerField()),
                ("film_id", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("one_time_password_id", models.IntegerField(auto_created=True)),
                ("login", models.CharField(max_length=15, unique=True)),
                ("password", models.CharField(max_length=25, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("first_name", models.CharField(max_length=20)),
                (
                    "location",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("YV", "Yerevan"),
                            ("ARM", "Armavir"),
                            ("AR", "Ararat"),
                            ("ART", "Ararat"),
                            ("KT", "Kotayk"),
                            ("SHI", "Shirak"),
                            ("LR", "Lorri"),
                            ("GK", "Geharkunik"),
                            ("SY", "Syunik"),
                            ("ARG", "Aragatsotn"),
                            ("TV", "Tavush"),
                            ("VD", "Vayoc Dzor"),
                            ("IT", "International"),
                        ],
                        max_length=30,
                        null=True,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("avatar", models.ImageField(upload_to="media/user/avatar")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_active", models.DateTimeField(auto_now=True)),
                ("comments", models.TextField(blank=True, null=True)),
                ("groups", models.CharField(max_length=30)),
                ("film_rating", models.SmallIntegerField()),
                ("film_history", models.SmallIntegerField()),
                ("bookmarks", models.SmallIntegerField()),
            ],
        ),
    ]
