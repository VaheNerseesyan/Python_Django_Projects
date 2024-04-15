from django.db import models

class Apartment(models.Model):
    location = models.CharField(max_length=30)
    house_type = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    currency = models.CharField(max_length=5)
    optional_description = models.TextField(max_length=500)
    total_area = models.PositiveIntegerField()
    rooms_count = models.PositiveIntegerField()
    bathrooms_count = models.PositiveIntegerField()
    furniture = models.CharField(max_length=20)
    ceiling_height = models.PositiveIntegerField()
    apartment_floor = models.PositiveIntegerField()
    apartment_repair = models.CharField(max_length=35)

    def __str__(self):
        return f"{self.location} - {self.price}"

class PrivateHouse(models.Model):
    location = models.CharField(max_length=30)
    house_type = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    currency = models.CharField(max_length=5)
    building_type = models.CharField(max_length=20)
    house_area = models.PositiveIntegerField()
    floor_count = models.PositiveIntegerField()
    rooms_count = models.PositiveIntegerField()
    bathrooms_count = models.PositiveIntegerField()
    furniture = models.CharField(max_length=20)
    garage = models.CharField(max_length=15)
    apartment_repair = models.CharField(max_length=35)
    total_area = models.PositiveIntegerField()
    status = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.location} - {self.price}"


class Land(models.Model):
    location = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    currency = models.CharField(max_length=5)
    land_area = models.PositiveIntegerField()
    service_lines = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.location} - {self.price} - {self.type}"


class GaragesAndParking(models.Model):
    location = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    floor_area = models.PositiveIntegerField()
    amenities = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.location} - {self.price} - {self.type}"

