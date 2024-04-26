from django.contrib import admin

from user.models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('login', 'email', 'first_name')
    list_display_links = ('login', 'email', 'first_name')


@admin.register(OneTimePassword)
class OneTimePasswordAdmin(admin.ModelAdmin):
    list_display = ('code', 'created_at')
    list_display_links = ('created_at',)
    list_editable = ('code', )

