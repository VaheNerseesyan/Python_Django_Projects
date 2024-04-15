from django.contrib import admin

from electronics.models import *

@admin.register(MobilePhones)
class MobilePhoneAdmin(admin.ModelAdmin):
    list_display = ('phone_model', "price", "storage_space", "color")
    list_display_links = ('phone_model', "price", "storage_space", "color")
    search_fields = ('phone_model', "price", "storage_space", "color", "condition")
    list_filter = ('phone_model', "price", "storage_space", "color", "condition")


@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    list_display = ('notebook_model', "price", "screen_size", "condition")
    list_display_links = ('notebook_model', "price", "screen_size", "condition")
    search_fields = ('notebook_model', "price", "screen_size", "condition")
    list_filter = ('notebook_model', "price", "screen_size", "condition")


@admin.register(Computers)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('product_details', "price", "condition")
    list_display_links = ('product_details', "price", "condition")
    search_fields = ('product_details', "price", "condition")
    list_filter = ('product_details', "price", "condition")


@admin.register(TV)
class TVAdmin(admin.ModelAdmin):
    list_display = ('tv_model', "price", "screen_size", "condition")
    list_display_links = ('tv_model', "price", "screen_size", "condition")
    search_fields = ('tv_model', "price", "screen_size", "condition")
    list_filter = ('tv_model', "price", "screen_size", "condition")

