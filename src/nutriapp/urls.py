from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .utils import check_token


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="NutriApp API ",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="rafayotuel@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('api/v1.0/', include('patients.urls')),
    path('api/v1.0/', include('nutritionists.urls')),
    path('api/v1.0/', include('appointments.urls')),

    path('api/v1/login/', include('rest_social_auth.urls_jwt')),
    path('api/v1/login/', include('rest_social_auth.urls_token')),
    path('api/v1/login/', include('rest_social_auth.urls_session')),
    path('api/v1/auth/', include('rest_framework_social_oauth2.urls')),
    path('api/v1/check/', check_token),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
