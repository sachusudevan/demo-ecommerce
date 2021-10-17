
from django.conf.urls import url
from django.urls import path, include
from . import views
app_name = 'search'

urlpatterns = [
    path('', views.SearchResults, name="SearchResults"),
]
