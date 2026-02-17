"""
URL configuration for PCPartsIreland project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pcpartsireland.views import set_currency
from pathlib import Path
from django.views import View
from django.http import HttpResponse

class RobotsView(View):
    def get(self, request):
        robots_path = Path(settings.BASE_DIR) / "robots.txt"
        with open(robots_path) as f:
            return HttpResponse(f.read(), content_type="text/plain")


class SitemapView(View):
    def get(self, request):
        sitemap_path = Path(settings.BASE_DIR) / "sitemap.xml"
        with open(sitemap_path) as f:
            return HttpResponse(f.read(), content_type="application/xml")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path("accounts/", include("allauth.urls")),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('set-currency/<str:currency_code>/', set_currency, name='set_currency'),
    path("", include("form.urls")),
    path("faq/", include("faq.urls")),
    path("robots.txt", RobotsView.as_view()),
    path("sitemap.xml", SitemapView.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)