from django.urls import path
from apps.home.views import HomeView

urlpatterns = [
    path('', HomeView.as_view()),
    path('home/', HomeView.as_view()),
]