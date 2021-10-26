"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import views as auth_views

schema_view = get_schema_view(
   openapi.Info(
      title="Project Bitlab API",
      default_version='v1',
      description="There could be your add",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ers.imanbek@gmail.com"),
      license=openapi.License(name="Project Bitlab License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

swagger_patterns = [
   url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('swagger/', include(swagger_patterns)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('posts/', include('posts.urls')),
    path('comment/', include('comment.urls')),
    path('change_pass/', auth_views.PasswordChangeView.as_view()),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('likes/', include('likes.urls')),
    path('auth/', include('django.contrib.auth.urls')),
]