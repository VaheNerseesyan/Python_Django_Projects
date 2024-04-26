from django.contrib import admin

from candidate.models import *

# Register your models here.
@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):
    list_display = ('name_surname', "telephone_number", "activated_status")
    list_display_links = ('name_surname', "telephone_number")
    list_editable = ("activated_status", )
    search_fields = ("created_at", "updated_at")


@admin.register(CandidateADD)
class CandidateADDAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'position', 'created_at', 'updated_at')
    list_display_links = ('company_name', 'position', 'created_at', 'updated_at')
    search_fields = ('company_name', 'created_at', 'updated_at')

