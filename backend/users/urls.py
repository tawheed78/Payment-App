# from django.urls import path
# from .views import register_user, user_login, user_logout
# from django.views.generic import TemplateView

# urlpatterns = [
#     path('register/', register_user, name='register'),
#     path('login/', user_login, name='login'),
#     path('logout/', user_logout, name='logout'),
# ]

# urls.py
from django.urls import path
from .views import register_user, user_login, user_logout
from django.views.generic import TemplateView

urlpatterns = [
    # API Endpoints
    path('api/register/', register_user, name='api-register'),
    path('api/login/', user_login, name='api-login'),
    path('api/logout/', user_logout, name='api-logout'),

    # HTML Views
    path('register/', TemplateView.as_view(template_name='register.html'), name='register'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('logout/', user_logout, name='logout'),
]
