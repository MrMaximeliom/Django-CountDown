
from django.contrib import admin
from django.urls import path, include
from apps.home import urls as home_urls
from apps.accounts import urls as accounts_urls
urlpatterns = [
    path("", include(home_urls)),
    path("accounts/", include(accounts_urls)),
    path('admin/', admin.site.urls),

]
