from django.conf.urls import url

from .views import weather

urlpatterns = [
    url(r'^(?P<location>.+)/(?P<days_str>\d+)/$', weather)
]
