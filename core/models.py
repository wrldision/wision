from typing import ClassVar
from django.db import models
from django.db.models.fields import CharField, EmailField
from django.db.models.fields.files import ImageField
from django.views.generic import detail
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.deletion import CASCADE
from enum import Enum

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
    type = models.CharField(max_length=40, choices=[(idx.name, idx.value) for idx in TypeBesoin.all()])
    montant = models.IntegerField(help_text="Valeur en Dollars (USD)")
    detail =  models.TextField(default="Aucun Detail")

    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now= True)
    def __str__(self):
        return f"{self.id}"


class Besoin(models.Model):
    titre = models.CharField(max_length=40)
    resume = models.CharField(max_length=255)
    description = models.TextField(default="Aucune Description")
    type = models.CharField(max_length=40, choices=[(idx.name, idx.value) for idx in TypeBesoin.all()])

    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now= True)
    def __str__(self):
        return f"{self.titre}"