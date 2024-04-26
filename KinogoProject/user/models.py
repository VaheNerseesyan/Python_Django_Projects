from django.db import models


LOCATION_AREA = (
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
    ("IT", "International")
)

# Create your models here.
class User(models.Model):
    login = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)
    one_time_password_id = models.IntegerField(auto_created=True)
    first_name = models.CharField(max_length=20)
    location = models.CharField(
        max_length=30,
        choices=LOCATION_AREA,
        null=True,
        blank=True
    )
    description = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to='media/user/avatar')
    created_at = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    comments = models.TextField(null=True, blank=True)
    groups = models.CharField(max_length=30)
    film_rating = models.SmallIntegerField()
    film_history = models.SmallIntegerField()
    bookmarks = models.SmallIntegerField()

    def __str__(self):
        return self.login


class OneTimePassword(models.Model):
    user_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    attempted_left = models.SmallIntegerField()

    def __str__(self):
        return self.code


class RatedFilms(models.Model):
    rate = models.SmallIntegerField()
    film_id = models.IntegerField()

class HistoryViews(models.Model):
    view_date = models.DateTimeField()
    film_id = models.IntegerField()

class Bookmarks(models.Model):
    count = models.SmallIntegerField()
    film_id = models.IntegerField()


