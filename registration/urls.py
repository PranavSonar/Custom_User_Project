from django.urls import path
from .views import LoginView, SignupView

app_name = 'registration'

urlpatterns = [
    path('', SignupView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
]
