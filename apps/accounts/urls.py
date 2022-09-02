from django.urls import path
from apps.accounts.views import LogInView,RegisterView

urlpatterns = [
    path('login', LogInView.as_view()),
    path('register', RegisterView.as_view()),
]