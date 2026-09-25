
from django.urls import path, include
from .views import market_view, markets_single_view, seller_view, sellers_single_view

urlpatterns = [
    path('market/', market_view),
    path('market/<int:pk>/', markets_single_view),
    path('seller/', seller_view),
    path('seller/<int:pk>/', sellers_single_view, name='seller_single')
]
