# stations/views.py
from django.shortcuts import render, redirect
from .models import Station
from django.utils import timezone
from datetime import timedelta

def home(request):
    # 🕒 Auto-delete old stations (older than 12 hours)
    twelve_hours_ago = timezone.now() - timedelta(hours=12)
    Station.objects.filter(created_at__lt=twelve_hours_ago).delete()

    if request.method == "POST":
        name = request.POST.get("station-name")
        location = request.POST.get("location")
        status = request.POST.get("status")
        if name and location and status:
            Station.objects.create(name=name, location=location, status=status)
        return redirect('home')

    stations = Station.objects.all().order_by('-created_at')
    return render(request, "home.html", {"stations": stations})





from django.http import HttpResponse

def robots_txt(request):
    content = (
        "User-agent: *\n"
        "Disallow:\n"
        "\n"
        "Sitemap: https://fuelfindermali-production.up.railway.app/sitemap.xml\n"
    )
    return HttpResponse(content, content_type="text/plain")


