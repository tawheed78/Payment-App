from django.urls import path
from .views import razorpay_payment_view, home_view, paypal_payment_view, paypal_payment_success_view, razorpay_payment_success_view
# success_view, cancel_view, stripe_checkout_view,

urlpatterns = [
    path('home/', home_view, name='home_view'),
    
    path('payment/razorpay/', razorpay_payment_view, name='payment-razorpay'),
    path('payment/razorpay/success/', razorpay_payment_success_view, name='payment-success'),

    path('payment/paypal/', paypal_payment_view, name='payment-paypal'),
    path('payment/paypal/success/', paypal_payment_success_view, name='payment-success'),
]
 # path('create-checkout-session/', stripe_checkout_view, name='create_checkout_session'),
    # path('payment/success/', success_view, name='success_view'),
    # path('payment/cancel/', cancel_view, name='cancel_view'),