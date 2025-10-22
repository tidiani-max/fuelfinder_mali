from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# stations/views.py
from django.shortcuts import render, redirect
from .models import Station

def home(request):
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
    content = """
    User-agent: *
    Disallow:

    Sitemap: https://fuelfindermali-production.up.railway.app/sitemap.xml
    """
    return HttpResponse(content, content_type="text/plain")

