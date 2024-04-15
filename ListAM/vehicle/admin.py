from django.contrib import admin


from vehicle.models import *


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "brand", "comp", "color", "year", "price")
    list_display_links = ("model", "brand")
    search_fields = ("model", "brand", "year", "price")
    list_filter = ("model", "brand", "year", "price")


@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ("model", "brand", "color", "year", "price")
    list_display_links = ("model", "brand")
    search_fields = ("model", "brand", "year", "price")
    list_filter = ("model", "brand", "year", "price")


@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    list_display = ("model", "brand", "color", "year", "price")
    list_display_links = ("model", "brand")
    search_fields = ("model", "brand", "year", "price")
    list_filter = ("model", "brand", "year", "price")


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ("model", "brand", "color", "year", "price")
    list_display_links = ("model", "brand")
    search_fields = ("model", "brand", "year", "price")
    list_filter = ("model", "brand", "year", "price")


@admin.register(SpecialTechnic)
class SpecialTechnicAdmin(admin.ModelAdmin):
    list_display = ("model", "year", "price")
    list_display_links = ("model", "year")
    search_fields = ("model", "year", "price")
    list_filter = ("model", "year", "price")


@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ("model", "brand", "comp", "color", "year", "price")
    list_display_links = ("model", "brand")
    search_fields = ("model", "brand", "year", "price")
    list_filter = ("model", "brand", "year", "price")


