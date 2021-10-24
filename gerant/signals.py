from .models import Gerant
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#Les signals permettent a des applications 
# django de communiquer entre elle lorsqu'un 
#changement oppère au niveau d'une d'entre elle

@receiver(post_save, sender = User)
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        Gerant.objects.create(user = instance)