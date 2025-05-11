from django.urls import path
from station.views import BusViewSet
from rest_framework import routers

app_name ="station"

router = routers.DefaultRouter()
router.register("buses", BusViewSet)

urlpatterns = router.urls
