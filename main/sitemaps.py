
# main/sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    protocol = "https"  # Force HTTPS instead of HTTP

    
    def items(self):
        # List of named URLs you want indexed
        return ['home']

    def location(self, item):
        return reverse(item)

sitemaps = {
    'static': StaticViewSitemap,
}
