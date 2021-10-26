from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, LoginViewSet
from users.views.logout import BlacklistRefreshView

router = DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('login/', LoginViewSet.as_view()),
    path('logout/', BlacklistRefreshView.as_view(), name="logout"),
] + router.urls
