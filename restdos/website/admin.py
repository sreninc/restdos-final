from django.contrib import admin
from .models import Signup

# Register your models here.
class SignupAdmin(admin.ModelAdmin):
    list_display = (
        'account_number',
        'first_name',
        'last_name',
        'email',
        'mobile',
        'signup_plan',
        'signup_monthly',
    )

admin.site.register(Signup, SignupAdmin)