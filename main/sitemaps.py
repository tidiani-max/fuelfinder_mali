# main/sitemaps.py (Temporary testing code)
from django.contrib.sitemaps import Sitemap

# Do not import Station model
# from .models import Station 

class StationSitemap(Sitemap):
    # This will just create one link for the home page.
    def items(self):
        return ['home']

    def location(self, item):
        return '/'

sitemaps = {
    'test': StationSitemap, # Use 'test' instead of 'stations'
}
# Keep your urls.py the same, but it will use the new 'sitemaps' dictionary.
