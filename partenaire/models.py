from django.db import models
from django.db.models.fields import CharField, EmailField
from django.db.models.fields.files import ImageField
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.deletion import CASCADE


class Partenaire(models.Model):
    nom_organisation = models.CharField(max_length=40)
    logo_partenaire= models.ImageField(upload_to ='logo', default = 'noimage.png' )
    description = models.TextField(default="Aucune Description")
    email1 = models.EmailField()
    email2 = models.EmailField(blank=True)
    tel1 = PhoneNumberField()
    tel2 = PhoneNumberField(blank=True)
    
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now= True)
    def __str__(self):
        return f"{self.nom_organisation}"

# Create your models here.
