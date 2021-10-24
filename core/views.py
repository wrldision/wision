from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from .models import Don, Besoin
from partenaire.models import Partenaire


# Create your views here.
def home_view(request):
    PartenaireQueryLatest = None
    BesoinQueryLatest = None
    DonQueryLatest = None

    PartenaireQueryLatest = Partenaire.objects.all().order_by('-created_at')[:9] #Les 09 Derniers Partenaire
    BesoinQueryLatest = Besoin.objects.all().order_by('-created_at')[:9] #Les 09 Derniers Besoins
    DonQueryLatest = Don.objects.all().order_by('-created_at')[:9] #Les 09 Derniers Dons

    context = {
        'PartenaireQueryLatest': PartenaireQueryLatest,
        'BesoinQueryLatest':BesoinQueryLatest,
        'DonQueryLatest':DonQueryLatest,
        #'':,
    }
    return render(request, 'core/home.html', context)




