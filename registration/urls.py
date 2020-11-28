from django.urls import path
from .views import SignupView
from django.contrib.auth import views as auth_views

app_name = 'registration'

urlpatterns = [
    path('', SignupView.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
