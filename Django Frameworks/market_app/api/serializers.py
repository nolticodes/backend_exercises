from rest_framework import serializers
from market_app.models import Market, Seller

def validate_noX(value):
        errors = []

        if 'X' in value:
            errors.append('no X in location')
        
        if 'Y' in value:
            errors.append('no Y in location')
                                              
        if errors:
            raise serializers.ValidationError(errors)

        return value

class MarketSerializer(serializers.ModelSerializer):

    class Meta:
         model = Market
         fields = '__all__'

    def validate_location(self, value):
        return validate_noX(value)


class SellerDetailsSerializer(serializers.Serializer):
     id = serializers.IntegerField(read_only = True)
     name = serializers.CharField(max_length = 255)
     contact_info = serializers.CharField()
    #  markets = MarketSerializer(many = True, read_only = True)
     markets = serializers.StringRelatedField(many = True)

class SellerCreateSerializer(serializers.Serializer):
     name = serializers.CharField( max_length = 255)
     contact_info = serializers.CharField(max_length = 255)
     markets = serializers.ListField(child=serializers.IntegerField(), write_only = True)
     

     def validate_markets(self, value):
        markets = Market.objects.filter(id__in = value)
        if len(markets) != len(value):
             raise serializers.ValidationError('one or more markets not found')
        return value

     def create(self, validated_data):
          market_ids = validated_data.pop('markets')
          seller = Seller.objects.create(**validated_data)
          markets = Market.objects.filter(id__in=market_ids)
          seller.markets.set(markets)
          return seller
