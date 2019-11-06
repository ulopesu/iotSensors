from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from iotSensors.api import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'unit', views.UnitViewSet)
router.register(r'sensor', views.SensorViewSet)
router.register(r'stream', views.StreamViewSet)
router.register(r'data', views.DataViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/<int:id>/getSensors/', views.getSensors),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]