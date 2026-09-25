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

    sellers = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name='seller_single')

    class Meta:
         model = Market
         exclude = []

    def validate_location(self, value):
        return validate_noX(value)

class SellerSerializer(serializers.ModelSerializer):
     markets = MarketSerializer(many = True, read_only = True)
     market_ids = serializers.PrimaryKeyRelatedField(
          queryset = Market.objects.all(),
          many = True,
          write_only = True,
          source = 'markets'
     )

     market_count = serializers.SerializerMethodField()

     class Meta:
          model = Seller
          fields = ["id", "name", "market_count", "market_ids", "markets", "contact_info",]

     def get_market_count(self, obj):
          return obj.markets.count()
     
    