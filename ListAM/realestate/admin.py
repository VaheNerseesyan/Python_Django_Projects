from django.contrib import admin

from realestate.models import *

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ("location", "price", "total_area", "rooms_count", "bathrooms_count", "apartment_floor")
    list_display_links = ("location", "total_area", "price")
    search_fields = ("location", "price", "rooms_count")
    list_filter = ("location", "price", "total_area", "rooms_count", "bathrooms_count", "apartment_floor")


@admin.register(PrivateHouse)
class PrivateHouseAdmin(admin.ModelAdmin):
    list_display = ("location", "price", "total_area", "house_area", "rooms_count", "bathrooms_count")
    list_display_links = ("location", "price", "total_area", "house_area", "rooms_count", "bathrooms_count")
    search_fields = ("location", "price", "total_area", "house_area", "rooms_count")
    list_filter = ("location", "price", "total_area", "house_area", "rooms_count", "bathrooms_count")


@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    list_display = ("location", "type", "price", "land_area")
    list_display_links = ("location", "type", "price", "land_area")
    search_fields = ("location", "type", "price", "land_area")
    list_filter = ("location", "type", "price", "land_area")

@admin.register(GaragesAndParking)
class GaragesAndParkingAdmin(admin.ModelAdmin):
    list_display = ("location", "type", "price", "amenities")
    list_display_links = ("location", "type", "price", "amenities")
    search_fields = ("location", "type", "price", "amenities")
    list_filter = ("location", "type", "price", "amenities")

