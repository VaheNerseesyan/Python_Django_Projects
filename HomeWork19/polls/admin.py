from django.contrib import admin
from django.utils.safestring import mark_safe

from polls.models import Phone, Owner


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'memory', 'created_at', 'status', 'get_image')
    list_display_links = ("id", 'model',)
    list_filter = ('model', 'created_at', 'color', 'status')
    search_fields = ('model', 'color', 'memory')
    readonly_fields = ('get_image',)
    save_on_top = True
    list_editable = ('status',)
    fieldsets = (
        ('Model', {
            'fields': (('model', 'memory'),)
        }),
        ('Color and Photo', {
            'fields': (('color', 'photo'),)
        })
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="100" height="70"')

    get_image.short_description = 'Photo'


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('phone', 'phone_models')
    list_display_links = ('phone', 'phone_models')
    search_fields = ('phone',)

