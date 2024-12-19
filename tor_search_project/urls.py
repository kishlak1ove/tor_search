from django.contrib import admin
from django.urls import path
from search.views import search_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', search_url, name='search_url'),
]