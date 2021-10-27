from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class Donateur(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    bio = models.TextField(default="Aucune biographie...")
    email = models.EmailField()
    nom = models.CharField(max_length=40)
    prenom = models.CharField(max_length=40)
    avatar = models.ImageField(upload_to ='avatars', default = 'avatar.png' )

    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now= True)

    def __str__(self):
        return f"Profil de {self.user.username}"