from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView

# Create your views here.

class SignupView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('registration:index')

    def form_valid(self, form):
        valid = super(SignupView, self).form_valid(form)
        email, password = form.cleaned_data.get('email'), form.cleaned_data.get('password1')
        user = authenticate(email=email,
                            password=password)
        login(self.request, user)
        return valid
