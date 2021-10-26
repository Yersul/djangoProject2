from django.urls import path
from rest_framework.routers import DefaultRouter


from comment.views.comment import CommentViewSet

router = DefaultRouter()

router.register('', CommentViewSet)


urlpatterns = [
     ] + router.urls
