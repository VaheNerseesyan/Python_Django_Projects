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

CURRENCY = (
    ("Armenian dram", "AMD"),
    ("United States Dollars", "USD")
)


# Create your models here.
class EmployerProfile(models.Model):
    company_name = models.CharField(max_length=50, unique=True)
    avatar = models.ImageField(upload_to='media/employer/avatar')
    name_surname = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=20, unique=True)
    job_add_id = models.BigIntegerField(auto_created=True)
    status = models.BooleanField()


    def __str__(self):
        return self.company_name

class EmployerADD(models.Model):
    job_name = models.CharField(max_length=40)
    description = models.TextField(max_length=500)
    foreign_citizens = models.BooleanField()
    sector = models.CharField(max_length=40)
    remote_status = models.BooleanField()
    city = models.CharField(max_length=30, choices=LOCATION_AREA)
    job_time = models.CharField(max_length=30)
    experience = models.CharField(max_length=40)
    working_schedule = models.CharField(max_length=40)
    salary_start = models.CharField(max_length=40)
    salary_end = models.CharField(max_length=40)
    currency = models.CharField(max_length=25, choices=CURRENCY)
    frequency = models.CharField(max_length=20)
    application_deadline = models.CharField(max_length=40)
    application_procedure = models.CharField(max_length=40)
    status = models.BooleanField()

    def __str__(self):
        return self.job_name


