from django.urls import path

from . import views

urlpatterns = [
    path('currencies/', views.CurrencyAPIViewSet.as_view({'get': 'list'}), name='currency-list'),
    path('currency/<int:pk>', views.CurrencyAPIViewSet.as_view({'get': 'retrieve'})),

]

