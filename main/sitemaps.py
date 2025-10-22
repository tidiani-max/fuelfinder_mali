# main/sitemaps.py
from django.contrib.sitemaps import Sitemap
from .models import Station

class StationSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.8

    def items(self):
        # *** CHANGE THIS LINE ***
        return Station.objects.all().order_by('-created_at') # Order by most recently created

    def lastmod(self, obj):
        return obj.created_at
