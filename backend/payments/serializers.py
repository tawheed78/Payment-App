from rest_framework import serializers
from .models import Transaction, PaymentToken

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('__all__')


class PaymentTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentToken
        fields = ('__all__')