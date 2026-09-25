
from django.urls import path, include
from .views import market_view, markets_single_view, seller_view, sellers_single_view, MarketView, SellerView

urlpatterns = [
    path('market/', MarketView.as_view()),
    path('market/<int:pk>/', markets_single_view, name='market-detail'),
    path('seller/', SellerView.as_view()),
    path('seller/<int:pk>/', sellers_single_view, name='seller_single')
]
