from .views import RegisterAPI, SignUpView, LoginAPI 

from django.urls import path

from knox.views import LogoutView, LogoutAllView 

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', LogoutView, name='logout'),
    path('api/logoutall/', LogoutAllView, name='logoutall'),
    path('signup/', SignUpView.as_view(), name='signup'),
]