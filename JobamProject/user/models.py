from django.db import models

# Create your models here.
class OneTimeURL(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    attepted_left = models.PositiveSmallIntegerField()
    url = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.url

