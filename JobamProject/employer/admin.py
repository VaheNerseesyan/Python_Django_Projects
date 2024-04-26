from django.contrib import admin

from employer.models import *
# Register your models here.
@admin.register(EmployerProfile)
class EmployerProfileAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'phone_number', 'status')
    list_display_links = ('company_name', 'phone_number')
    list_editable = ('status',)


@admin.register(EmployerADD)
class EmployerADDAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'remote_status', 'salary_start', 'salary_end', 'status')
    list_display_links = ('job_name', 'salary_start', 'salary_end')
    list_editable = ('remote_status', 'status')



