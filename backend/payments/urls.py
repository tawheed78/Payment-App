from django.urls import path
from .views import payment_view, payment_success_view, home_view, success_view, cancel_view, stripe_checkout_view

urlpatterns = [
    path('home/', home_view, name='home_view'),
    path('payment/', payment_view, name='payment'),
    path('payment/success/', payment_success_view, name='payment_success'),

    path('create-checkout-session/', stripe_checkout_view, name='create_checkout_session'),
    path('payment/success/', success_view, name='success_view'),
    path('payment/cancel/', cancel_view, name='cancel_view'),
]
