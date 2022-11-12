from rest_framework import serializers
from .models import *


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = "__all__"


class CommuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commune
        fields = "__all__"


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = "__all__"


class QuartierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quartier
        fields = "__all__"


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"


class VenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vente
        fields = "__all__"


class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = "__all__"


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"


class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = "__all__"


class VenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vente
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class MutuelleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mutuelle
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        
class AgenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agence
        fields = "__all__"

class DetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dette
        fields = "__all__"
