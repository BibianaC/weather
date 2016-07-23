from django.conf.urls import include, url
from django.contrib import admin

from weather import urls as weather_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v0/', include(weather_urls)),
]
