from rest_framework import serializers
from .models import *


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = "__all__"
        # exclude=["user"]


class CommuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commune
        fields = "__all__"
        

    def to_representation(self, obj):
        serializer=super().to_representation(obj)
        # serializer["user"]=obj.user.username
        serializer["province"]=str(obj.province)
        return serializer
    
class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = "__all__"
    
    def to_representation(self, obj):
        serializer=super().to_representation(obj)
        # serializer["user"]=obj.user.username
        serializer["commune"]=str(obj.commune)
        return serializer


class QuartierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quartier
        fields = "__all__"
        
    def to_representation(self, obj):
        serializer=super().to_representation(obj)
        # serializer["user"]=obj.user.username
        serializer["zone"]=str(obj.zone)
        return serializer

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"
    
    def to_representation(self, obj):
        serializer=super().to_representation(obj)
        # serializer["user"]=obj.user.username
        serializer["agence"]=str(obj.agence)
        return serializer

class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = "__all__"
    
    def to_representation(self, obj):
        serializer=super().to_representation(obj)
        # serializer["user"]=obj.user.username
        serializer["agence"]=str(obj.agence)
        return serializer
class BasicPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = "id", "nom_personnel" , "prenom_personnel" , "phone_personnel"
    
    

class VenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vente
        fields = "__all__"
        
    def to_representation(self, obj):
        serializer=super().to_representation(obj)
        # serializer["user"]=obj.user.username
        serializer["agence"]=str(obj.agence)
        # serializer["client"]=ClientSerializer(obj.client).data
        serializer["personnel"]=BasicPersonnelSerializer(obj.personnel).data
        # serializer["produit"]= ProduitSerializer(obj.produit).data
        
        return serializer




class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = "__all__"
    
    def to_representation(self, obj):
        serializer=super().to_representation(obj)
        # serializer["user"]=obj.user.username
        serializer["stock"]=str(obj.stock)
        return serializer


# class VenteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vente
#         fields = "__all__"


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
    
    def to_representation(self, obj):
        serializer=super().to_representation(obj)
        # serializer["user"]=obj.user.username
        serializer["quartier"]=str(obj.quartier)
        return serializer

class DetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dette
        field = "__all__"
