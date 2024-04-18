from django.contrib import admin

from realestate.models import *


@admin.register(LongTermApartmentRentals)
class LongTermApartmentRentalsAdmin(admin.ModelAdmin):
    list_display = ("location", "price", "verified_ads")
    list_display_links = ("location", "price")
    search_fields = ("location", "price")
    list_filter = ("location", "price", "apartment_floor")
    save_on_top = True
    save_as_continue = True
    list_editable = ("verified_ads",)


@admin.register(LongTermRentalsHouse)
class LongTermRentalsHouseAdmin(admin.ModelAdmin):
    list_display = ("location", "price", "verified_ads")
    list_display_links = ("location", "price")
    search_fields = ("location", "price")
    list_filter = ("location", "price")
    save_on_top = True
    save_as_continue = True
    list_editable = ("verified_ads",)


@admin.register(LongTermRentalsCommercialProperties)
class LongTermRentalsCommercialPropertiesAdmin(admin.ModelAdmin):
    list_display = ("location", "price", "verified_ads")
    list_display_links = ("location", "price")
    search_fields = ("location", "price")
    list_filter = ("location", "price")
    save_on_top = True
    save_as_continue = True
    list_editable = ("verified_ads",)
