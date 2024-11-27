from django.urls import include, path
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()

router.register('mobiles', views.MobileViewSet, basename='mobile')

urlpatterns = router.urls