from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from likes.views import LikesViewSet

router = DefaultRouter()

router.register('', LikesViewSet)

urlpatterns = [

    ] + router.urls
