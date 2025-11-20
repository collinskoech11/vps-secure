from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_and_request_access, name='register'),
    path('registration-complete/', views.registration_complete, name='registration_complete'),
]
