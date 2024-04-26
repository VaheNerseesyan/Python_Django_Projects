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
class CandidateProfile(models.Model):
    name_surname = models.CharField(
        max_length=50
    )
    email = models.EmailField(
        max_length=50,
        unique=True
    )
    password = models.CharField(
        max_length=25,
        unique=True
    )
    activated_status = models.BooleanField()
    avatar = models.ImageField(
        upload_to="media/candidate/avatar",
        null=True,
        blank=True
    )
    resume = models.TextField(
        max_length=1000
    )
    resume_file = models.FileField(
        upload_to="media/resume",
        null=True,
        blank=True
    )
    location = models.CharField(
        max_length=40,
        choices=LOCATION_AREA
    )
    address = models.CharField(
        max_length=50
    )
    birth_date = models.DateField()
    telephone_number = models.CharField(
        max_length=13
    )
    my_application_id = models.CharField(
        max_length=25,
        unique=True
    )

    def __str__(self):
        return self.name_surname


class CandidateADD(models.Model):
    company_name = models.CharField(
        max_length=40
    )
    avatar = models.ImageField(
        upload_to="media/candidate/avatar"
    )
    title = models.CharField(
        max_length=50
    )
    sector = models.CharField(
        max_length=40
    )
    deadline = models.DateTimeField()
    city = models.CharField(
        max_length=20,
        choices=LOCATION_AREA
    )
    position = models.CharField(
        max_length=30
    )
    salary = models.CharField(
        max_length=20
    )
    work_schedule = models.CharField(
        max_length=40
    )
    work_experience = models.CharField(
        max_length=40
    )
    description = models.TextField(
        max_length=1000
    )
    created_at = models.DateField()
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.company_name

