from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="EXCHANGE RATES API DOCS",
      default_version='v1',
      description="service for getting the exchange rate against the ruble",
      # terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="izolotavin99@sgmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.IsAuthenticated],
)

urlpatterns = [
   path('swagger(<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]