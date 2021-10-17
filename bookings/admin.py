from django.contrib import admin
from .models import Booking

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'time',
        'rating',
        'people',
    )

    ordering = ('date', 'time')


admin.site.register(Booking, BookingAdmin)