from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from iotSensors.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'units', views.UnitsViewSet)
router.register(r'sensor', views.SensorViewSet)
router.register(r'stream', views.StreamViewSet)
router.register(r'data', views.DataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]