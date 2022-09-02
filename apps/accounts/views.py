from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class LogInView(TemplateView):
    template_name = "accounts/login.html"

class RegisterView(TemplateView):
    template_name = "accounts/register.html"