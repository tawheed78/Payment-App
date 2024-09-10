from django.urls import path
from .views import payment_view, payment_success_view, home_view

urlpatterns = [
    path('home/', home_view, name='home_view'),
   path('payment/', payment_view, name='payment'),
   path('payment/success/', payment_success_view, name='payment_success'),
]
