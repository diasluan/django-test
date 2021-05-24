from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"timezones", views.TimezoneViewSet, basename="Timezones")

urlpatterns = [
    path("", include(router.urls)),
]
