from datetime import timedelta

from django.contrib import messages
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone

from .models import Station


# ============================================================
# RATE-LIMITING CONFIGURATION
# ============================================================

RATE_LIMIT_MAX_SUBMISSIONS = 5
RATE_LIMIT_WINDOW_SECONDS = 15 * 60


def get_client_ip(request):
    """
    Get the client's IP address.

    Uses X-Forwarded-For when available behind a reverse proxy.
    Falls back to REMOTE_ADDR.
    """

    forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

    if forwarded_for:
        return forwarded_for.split(",")[0].strip()

    return request.META.get("REMOTE_ADDR", "unknown")


def get_rate_limit_key(request):
    """
    Generate a unique Redis cache key for the submitting client.
    """

    client_ip = get_client_ip(request)

    return f"station-submission-rate-limit:{client_ip}"


def can_submit_station(request):
    """
    Enforce a maximum of five submissions within 15 minutes.

    Returns:
        True: Submission is allowed.
        False: Submission limit has been reached.
    """

    cache_key = get_rate_limit_key(request)

    current_count = cache.get(cache_key, 0)

    if current_count >= RATE_LIMIT_MAX_SUBMISSIONS:
        return False

    if current_count == 0:
        cache.set(
            cache_key,
            1,
            timeout=RATE_LIMIT_WINDOW_SECONDS,
        )
    else:
        cache.incr(cache_key)

    return True


# ============================================================
# MAIN VIEW
# ============================================================

def home(request):
    """
    Display fuel stations and process new submissions.
    """

    # Delete stations older than 12 hours.
    twelve_hours_ago = timezone.now() - timedelta(hours=12)

    Station.objects.filter(
        created_at__lt=twelve_hours_ago
    ).delete()

    if request.method == "POST":

        # Apply server-side rate limiting.
        if not can_submit_station(request):
            messages.error(
                request,
                (
                    "Submission limit reached. "
                    "You can submit a maximum of five reports "
                    "within 15 minutes. Please try again later."
                ),
            )

            return redirect("home")

        name = request.POST.get("station-name", "").strip()
        location = request.POST.get("location", "").strip()
        status = request.POST.get("status", "").strip()

        if not name or not location or not status:
            messages.error(
                request,
                "Please complete all required fields.",
            )

            return redirect("home")

        valid_statuses = {
            choice[0]
            for choice in Station._meta.get_field("status").choices
        }

        if status not in valid_statuses:
            messages.error(
                request,
                "Invalid station status.",
            )

            return redirect("home")

        Station.objects.create(
            name=name,
            location=location,
            status=status,
        )

        messages.success(
            request,
            "Station submitted successfully.",
        )

        return redirect("home")

    stations = Station.objects.all().order_by("-created_at")

    return render(
        request,
        "home.html",
        {
            "stations": stations,
        },
    )


# ============================================================
# ROBOTS.TXT
# ============================================================

def robots_txt(request):
    """
    Return the robots.txt file.
    """

    content = (
        "User-agent: *\n"
        "Disallow:\n"
        "\n"
        "Sitemap: "
        "https://fuelfindermali-production.up.railway.app/"
        "sitemap.xml\n"
    )

    return HttpResponse(
        content,
        content_type="text/plain",
    )
