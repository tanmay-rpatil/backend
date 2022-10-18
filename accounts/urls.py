from django.urls import path
from .views import SignUpView, RegisterAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('signupui/', SignUpView.as_view(), name='signup'),
]