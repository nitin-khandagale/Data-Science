from django.urls import path
from .views import HomeViewSet


from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'people', HomeViewSet, basename='basename')
urlpatterns = router.urls
