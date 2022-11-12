from django.db import models
from unittest.util import _MAX_LENGTH

# Create your models here.


class Province(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom_province = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.nom_province}"


class Commune(models.Model):
    id = models.BigAutoField(primary_key=True)
    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    nom_commune = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.nom_commune} de la province {self.province.nom_province}"


class Zone(models.Model):
    id = models.BigAutoField(primary_key=True)
    commune = models.ForeignKey(Commune, on_delete=models.PROTECT)
    nom_zone = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.nom_zone} de la commune {self.commune.nom_commune} "


class Quartier(models.Model):
    id = models.BigAutoField(primary_key=True)
    zone = models.ForeignKey(Zone, on_delete=models.PROTECT)
    nom_quartier = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.nom_quartier} de la zone {self.zone.nom_zone} "


class Agence(models.Model):
    id = models.BigAutoField(primary_key=True)
    quartier = models.ForeignKey(Quartier, on_delete=models.CASCADE)
    nom_agence = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.nom_agence} du quartier {self.quartier.nom_quartier} "


class Personnel(models.Model):
    id = models.BigAutoField(primary_key=True)
    agence = models.ForeignKey(Agence, on_delete=models.PROTECT)
    nom_personnel = models.CharField(max_length=32)
    prenom_personnel = models.CharField(max_length=32)
    phone_personnel = models.CharField(max_length=32)
    sexe = models.CharField(max_length=10)
    cni = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.nom_personnel} {self.prenom_personnel} {self.phone_personnel} {self.sexe} {self.cni} {self.agence.nom_agence} "


class Stock(models.Model):
    id = models.BigAutoField(primary_key=True)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    nom_stock = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.nom_stock} {self.agence.nom_agence} "


class Produit(models.Model):
    id = models.BigAutoField(primary_key=True)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    nom_produit = models.CharField(max_length=40)
    prix_achat = models.IntegerField(default=0)
    dateexpiration = models.DateField

    def __str__(self):
        return f"{self.nom_produit} {self.prix_achat} {self.dateexpiration} {self.stock.nom_stock} "


class Mutuelle(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom_mutuelle = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nom_mutuelle}"


class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom_personnel = models.CharField(max_length=32)
    prenom_personnel = models.CharField(max_length=32)
    phone_personnel = models.CharField(max_length=32)
    sexe = models.CharField(max_length=10)
    cni = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.nom_personnel} {self.prenom_personnel} {self.phone_personnel} {self.sexe} {self.cni}"


class Vente(models.Model):
    id = models.BigAutoField(primary_key=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    valeur_total = models.IntegerField(default=0)
    a_payer = models.IntegerField(default=0)
    payer = models.IntegerField(default=0)
    a_payer = models.IntegerField(default=0)
    paid = models.BooleanField(default=True)
    date_vente = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nom_personnel} {self.prenom_personnel} {self.phone_personnel} {self.sexe} {self.cni}"


class Dette(models.Model):
    id = models.BigAutoField(primary_key=True)
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE)
    date_paye = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.nom_personnel} {self.prenom_personnel} {self.phone_personnel} {self.sexe} {self.cni}"
