from django.urls import path
from . import views
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from stations.sitemaps import StationSitemap

sitemaps = {
    'stations': StationSitemap,
}
urlpatterns = [
    path('', views.home, name='home'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django-sitemap'),
]


