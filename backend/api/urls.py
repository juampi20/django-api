from django.conf.urls import url, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r"heroes", HeroViewSet, basename='heroes')

urlpatterns = router.urls