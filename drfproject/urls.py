from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken import views
from .views import CustomAuthToken

schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="blog api description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [

    # Those urls will add login and logout buttons to the browsable API 
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Obtain auth token, to be used in TokenAuthentication
    path('obtain-auth-token/', CustomAuthToken.as_view()), 

    # ****************** factory urls ******************
    path('factory/', include('factory.urls')), 

    # admin site urls
    path('admin/', admin.site.urls),

    # for the API Documentation
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

