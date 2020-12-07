from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer
from django.contrib.auth.models import User



class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'last_login') # Added last_login

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Customer)