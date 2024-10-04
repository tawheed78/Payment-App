from django.db import models
import jwt
import datetime
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=25)
    amount = models.FloatField()
    payment_gateway = models.CharField(max_length=50)
    status = models.CharField(max_length=25, default='In Progress')
    timestamp = models.DateTimeField(auto_now=True)
    # token = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return f'Transaction {self.id} - {self.status}'

def generate_token(data):
        return jwt.encode(
            {"data": data, "exp": datetime.datetime.now() + datetime.timedelta(hours=1)},
            settings.SECRET_KEY, algorithm="HS256"
        )

def verify_token(token):
        try:
            decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return decoded["data"]
        except jwt.ExpiredSignatureError:
            return None

def fetch_transaction_by_order_id(order_id):
    try:
        transaction = Transaction.objects.get(order_id=order_id)
        data = {
            'order_id': transaction.order_id,
            'amount': transaction.amount,
            'payment_gateway': transaction.payment_gateway,
            'status': transaction.status,
            'timestamp': transaction.timestamp
        }
        return data
    except ObjectDoesNotExist:
        return None


def create_logs(user, order_id, amount, payment_gateway, timestamp, status):
    Transaction.objects.create(
        user = user,
        order_id = order_id,
        amount = amount,
        payment_gateway = payment_gateway,
        timestamp = timestamp,
        status = status
    )
    

