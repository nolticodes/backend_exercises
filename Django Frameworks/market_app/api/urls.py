
from django.urls import path, include
from .views import market_view, markets_single_view

urlpatterns = [
    path('', market_view),
    path('<int:pk>/', markets_single_view)
]
