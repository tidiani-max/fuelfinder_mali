from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StationSitemap

sitemaps = {
    'stations': StationSitemap,
}
urlpatterns = [
    # 1. PLACE SPECIFIC PATHS FIRST (sitemap.xml and robots.txt)
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django-sitemap'),
    path("robots.txt", views.robots_txt),
    
    # 2. PLACE THE GENERIC HOME PATH LAST
    path('', views.home, name='home'), 
]


