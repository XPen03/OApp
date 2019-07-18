from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pictures',views.PictureView)
urlpatterns = [
    path('',include(router.urls))
]