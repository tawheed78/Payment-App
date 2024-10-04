from django.contrib import admin
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'payment_gateway', 'timestamp', 'status')

admin.site.register(Transaction, TransactionAdmin)
