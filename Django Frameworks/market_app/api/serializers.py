from rest_framework import serializers
from market_app.models import Market, Seller, Product


def validate_noX(value):
    errors = []

    if 'X' in value:
        errors.append('no X in location')

    if 'Y' in value:
        errors.append('no Y in location')

    if errors:
        raise serializers.ValidationError(errors)

    return value

class ProductSerialozer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class MarketSerializer(serializers.ModelSerializer):

    sellers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Market
        exclude = []

    def validate_location(self, value):
        return validate_noX(value)

class MarketHyperSerializer(MarketSerializer, serializers.HyperlinkedModelSerializer):

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Market
        exclude = []


class SellerSerializer(serializers.ModelSerializer):
    markets = MarketSerializer(many=True, read_only=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(),
        many=True,
        write_only=True,
        source='markets'
    )

    market_count = serializers.SerializerMethodField()

    class Meta:
        model = Seller
        fields = ["id", "name", "market_count", "markets", "market_ids", "contact_info",]

    def get_market_count(self, obj):
        return obj.markets.count()


class SellerListSerializer(SellerSerializer, serializers.HyperlinkedModelSerializer):
    class Meta:
            model = Seller
            fields = ["id", "url", "name", "market_count", "market_ids", "contact_info",]