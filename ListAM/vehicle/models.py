from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    comp = models.CharField(max_length=20, help_text="Complectation of Car", default='FULL')
    color = models.CharField(max_length=20, help_text="Color of car")
    description = models.TextField(help_text="About the Car")
    year = models.CharField(max_length=5)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.model} - {self.brand} - {self.year}"

class Bike(models.Model):
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    color = models.CharField(max_length=20, help_text="Color of Bike")
    description = models.TextField(help_text="About the Bike")
    year = models.CharField(max_length=5)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.model} - {self.brand} - {self.year}"

class Boat(models.Model):
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    comp = models.CharField(max_length=20, help_text="Complectation of Boat", default='FULL')
    color = models.CharField(max_length=20, help_text="Color of Boat")
    description = models.TextField(help_text="About the Boat")
    year = models.CharField(max_length=5)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.model} - {self.brand} - {self.year}"

class Truck(models.Model):
    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    description = models.TextField(help_text="About the Truck")
    year = models.CharField(max_length=5)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.model} - {self.brand} - {self.year}"

class SpecialTechnic(models.Model):
    model = models.CharField(max_length=20)
    year = models.CharField(max_length=5)
    optional = models.TextField(help_text="About the Technic")
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.model} - {self.price} - {self.year}"

class Bus(models.Model):
    model = models.CharField(max_length=25)
    brand = models.CharField(max_length=20)
    comp = models.CharField(max_length=20, help_text="Complectation of Bus", default='FULL')
    passage = models.CharField(max_length=20)
    color = models.CharField(max_length=20, help_text="Color of Bus")
    description = models.TextField(help_text="About the Truck")
    year = models.CharField(max_length=5)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.model} - {self.brand} - {self.year}"

