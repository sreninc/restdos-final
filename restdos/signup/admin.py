from django.contrib import admin
from .models import Signup

# Register your models here.
class SignupAdmin(admin.ModelAdmin):
    readonly_fields = ('account_number',)

    list_display = ('account_number', 'first_name', 'email', 'mobile', 'signup_plan', 'signup_monthly',)

    ordering = ('account_number',)

admin.site.register(Signup, SignupAdmin)