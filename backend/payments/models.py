from django.db import models
import jwt
import datetime
from django.conf import settings


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    payment_gateway = models.CharField(max_length=50)
    status = models.CharField(max_length=25, default='In Progress')
    timestamp = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return f'Transaction {self.id} - {self.status}'
    

class PaymentToken(models.Model):
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # @staticmethod
    # def generate_token(data):
    #     return jwt.encode(
    #         {"data": data, "exp": datetime.datetime.now() + datetime.timedelta(hours=1)},
    #         settings.SECRET_KEY, algorithm="HS256"
    #     )

    # @staticmethod
    # def verify_token(token):
    #     try:
    #         decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    #         return decoded["data"]
    #     except jwt.ExpiredSignatureError:
    #         return None
        
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