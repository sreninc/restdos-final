from django.contrib import admin
from .models import Guest

# Register your models here.
class GuestAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'mobile',
        'rating',
        'guest_since',
    )

    ordering = ('first_name', 'last_name')


admin.site.register(Guest, GuestAdmin)