from typing import ClassVar
from django.db import models
from django.db.models.fields import CharField, EmailField
from django.db.models.fields.files import ImageField
from django.views.generic import detail
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.deletion import CASCADE
from gerant.models import Gerant
from donateur.models import Donateur
from enum import Enum
from .utils import autogenref
from django.utils import timezone


# Create your models here.

class TypeBesoin(Enum):
    ch1  = "Don en Nature"
    ch2  = "Don en Espèces"


    @classmethod
    def all(self):
        return [
            TypeBesoin.ch1, TypeBesoin.ch2
        ]

class Don(models.Model):
    ref =  models.CharField(max_length=12, blank=True)
    type = models.CharField(max_length=40, choices=[(idx.name, idx.value) for idx in TypeBesoin.all()])
    montant = models.IntegerField(help_text="Valeur en Dollars Americain(1 USD = 560FCA)")
    detail =  models.TextField(default="Aucun Detail")

    donateur = models.ForeignKey(Donateur, on_delete=models.CASCADE, blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now= True)
    def __str__(self):
        return f" Une personne à donnée : {self.montant} $(ref = {self.ref.capitalize()})"

    def save(self, *args, **kwargs):
        if self.ref == "":
            self.ref = autogenref()
        if self.created_at is None:
            self.created_at = timezone.now
        return super().save(*args, **kwargs)
    
    def get_user_from_id(self):# Reverse relationship
        obj_user = self.donateur_set.first() # Cette method retourne id de vente a partir de  la class Achat()
        return obj_user


class Besoin(models.Model):
    titre = models.CharField(max_length=40)
    resume = models.CharField(max_length=255)
    description = models.TextField(default="Aucune Description")
    type = models.CharField(max_length=40, choices=[(idx.name, idx.value) for idx in TypeBesoin.all()])
    image_mise_en_avant = models.ImageField(upload_to ='besoin', default = 'ibsnoimage.png' )

    gerant = models.ForeignKey(Gerant, on_delete=models.CASCADE, blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now= True)
    def __str__(self):
        return f"{self.titre}"