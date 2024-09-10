from django.contrib import admin
from .models import PaymentToken, Transaction
# Register your models here.
admin.site.register(Transaction)
admin.site.register(PaymentToken)