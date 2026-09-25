from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MarketSerializer, SellerSerializer, MarketHyperSerializer
from market_app.models import Market
from market_app.models import Seller
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

class MarketView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Market.objects.all()
    serializer_class = MarketSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SellerView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

@api_view(['GET', 'POST'])
def market_view(request):
    if request.method == 'GET':
        markets = Market.objects.all()
        serializer = MarketHyperSerializer(markets, many=True, context={'request': request})
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MarketSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'DELETE', 'PUT'])
def markets_single_view(request, pk):

    if request.method == 'GET':
        market = Market.objects.get(pk=pk)
        serializer = MarketSerializer(market, context={'request': request})
        return Response(serializer.data)

    if request.method == 'DELETE':
        market = Market.objects.get(pk=pk)
        serializer = MarketSerializer(market, context={'request': request})
        market.delete()
        return Response(serializer.data)

    if request.method == 'PUT':
        market = Market.objects.get(pk=pk)
        serializer = MarketSerializer(market, data=request.data, partial=True,context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'POST'])
def seller_view(request):
    if request.method == 'GET':
        sellers = Seller.objects.all()
        serializer = SellerSerializer(sellers, many=True, context={'request': request})
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'POST', 'PUT'])
def sellers_single_view(request, pk):
    if request.method == 'GET':
        seller = Seller.objects.get(pk=pk)
        serializer = SellerSerializer(seller, context={'request': request})
        return Response(serializer.data)
    if request.method == 'DELETE':
        seller = Seller.objects.get(pk=pk)
        serializer = SellerSerializer(seller, context={'request': request})
        seller.delete()
        return Response(serializer.data)
    if request.method == 'PUT':
        seller = Market.objects.get(pk=pk)
        serializer = SellerSerializer(seller, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors)
