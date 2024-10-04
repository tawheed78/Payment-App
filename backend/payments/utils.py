import razorpay
from django.conf import settings
import time, stripe
from decouple import config
from datetime import datetime
import pytz

client = razorpay.Client(auth=(settings.API_KEY, settings.API_SECRET))
# stripe.api_key = config('STRIPE_KEY')
YOUR_DOMAIN = 'http://127.0.0.1:8000'


def initiate_payment(amount, currency='INR'):
   data = {
       'amount': amount * 100, 
       'currency': currency,
       'payment_capture': '1'
   }
   response = client.order.create(data=data)
   return response['id']

def fetch_current_time():
    timezone = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(timezone)
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S %Z')
    return formatted_time

def fetch_current_time_in_sec():
    timestamp_in_seconds = int(time.time())
    return str(timestamp_in_seconds)


def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return checkout_session.url
    except Exception as e:
        return str(e)

