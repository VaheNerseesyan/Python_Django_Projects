from django.db import models

class MobilePhones(models.Model):
    location = models.CharField(max_length=20)
    phone_model = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    currency = models.CharField(max_length=5)
    storage_space = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    condition = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.location} - {self.phone_model} - {self.price} - {self.storage_space}"

class Notebook(models.Model):
    location = models.CharField(max_length=20)
    notebook_model = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    currency = models.CharField(max_length=5)
    screen_size = models.PositiveIntegerField()
    condition = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.location} - {self.notebook_model} - {self.price} - {self.screen_size}"


class Computers(models.Model):
    location = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    currency = models.CharField(max_length=5)
    product_details = models.CharField(max_length=20)
    condition = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.location} - {self.price} - {self.product_details}"


class TV(models.Model):
    location = models.CharField(max_length=20)
    tv_model = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    currency = models.CharField(max_length=5)
    screen_size = models.PositiveIntegerField()
    condition = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.location} - {self.tv_model} - {self.price} - {self.screen_size}"

