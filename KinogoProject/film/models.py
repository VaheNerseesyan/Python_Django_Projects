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

GENRE = (
    ("Biography", "Biography"),
    ("Detection", "Detection"),
    ("A Game", "A Game"),
    ("Melodrama", "Melodrama"),
    ("Adventures", "Adventures"),
    ("Talk Shows", "Talk Shows"),
    ("Film Noir", "Film Noir"),
    ("Action Movies", "Action Movies"),
    ("Children", "Children"),
    ("Story", "Story"),
    ("Music", "Music"),
    ("Romance", "Romance"),
    ("Thrillers", "Thrillers"),
    ("Fantasy", "Fantasy"),
    ("Western", "Western"),
    ("Documentary", "Documentary"),
    ("Comedy", "Comedy"),
    ("Family", "Family"),
    ("Horror", "Horror"),
    ("Military", "Military"),
    ("Drama", "Drama"),
    ("Crime", "Crime"),
    ("News", "News"),
    ("Sport", "Sport"),
    ("Fantastic", "Fantastic")
)

# Create your models here.
class Film(models.Model):
    name = models.CharField(max_length=50)
    year_of_issue = models.DateField()
    location = models.CharField(max_length=50, choices=LOCATION_AREA)
    film_genre = models.CharField(max_length=25, choices=GENRE)
    duration = models.DateTimeField()
    premiere = models.DateField()
    quality = models.CharField(max_length=20)
    about_film = models.TextField(max_length=500)
    views = models.SmallIntegerField()
    comments = models.SmallIntegerField()
    votes = models.SmallIntegerField()

    def __str__(self):
        return self.name

