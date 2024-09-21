from django.contrib import admin
from .models import CustomUser
from payments.models import Transaction
# Register your models here.

admin.site.register(CustomUser)
