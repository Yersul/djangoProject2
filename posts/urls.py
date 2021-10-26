from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from posts.views import BlogViewSet, UpdatePostView, BlogModerateViewSet

router = DefaultRouter()

router.register('', BlogViewSet)
router.register('moderate', BlogModerateViewSet)

urlpatterns = [
    # path('get/', BlogModerateViewSet.as_view({'get': 'retrieve'})),
] + router.urls
