from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
from . import views

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django-sitemap"),
    path("robots.txt", views.robots_txt, name="robots-txt"),
    path("", views.home, name="home"),
]



