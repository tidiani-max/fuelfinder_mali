# stations/sitemaps.py
from django.contrib.sitemaps import Sitemap
from .models import Station

class StationSitemap(Sitemap):
    changefreq = "hourly"  # The status can change often
    priority = 0.8

    def items(self):
        return Station.objects.all()

    def lastmod(self, obj):
        return obj.created_at
