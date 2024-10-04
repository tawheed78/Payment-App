from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'phone_number', 'is_staff')
    readonly_fields = ('id',)
admin.site.register(CustomUser, CustomUserAdmin)
