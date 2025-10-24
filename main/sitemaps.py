# main/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StationSitemap(Sitemap):   # 👈 restore the name
    protocol = "https"

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)

sitemaps = {
    'static': StationSitemap,
}
