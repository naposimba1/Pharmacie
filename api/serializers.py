from rest_framework import serializers
from .models import *


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        field = "__all__"


class CommuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commune
        field = "__all__"


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        field = "__all__"


class QuartierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quartier
        field = "__all__"


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        field = "__all__"


class VenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vente
        field = "__all__"


class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        field = "__all__"


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        field = "__all__"


class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        field = "__all__"


class VenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vente
        field = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        field = "__all__"


class MutuelleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mutuelle
        field = "__all__"

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        field = "__all__"
