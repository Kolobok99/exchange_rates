from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views

urlpatterns = [
    path('currencies/', views.CurrencyAPIViewSet.as_view({'get': 'list'}), name='currency-list'),
    path('currency/<int:pk>', views.CurrencyAPIViewSet.as_view({'get': 'retrieve'})),

    path('api-token-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token-auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]


