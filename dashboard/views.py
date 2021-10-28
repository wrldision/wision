from django.shortcuts import redirect, render
from core.models import Don
from partenaire.models import Partenaire
from donateur.models import Donateur
from gerant.models import Gerant

# Create your views here.

def home_view(request):
    nbr_partenaires = Partenaire.objects.count()
    nbr_donateurs = Donateur.objects.count()
    nbr_gerants = Gerant.objects.count()

    # Nombre de personne s'étend connecter au dashboard
    nbr_visiteurs = request.session.get('nbr_visiteurs', 0)
    request.session['nbr_visiteurs'] = nbr_visiteurs + 1

    context = {
        'nbr_partenaires': nbr_partenaires,
        'nbr_donateurs': nbr_donateurs,
        'nbr_gerants': nbr_gerants,
        'nbr_visiteurs': nbr_visiteurs,
        #'':,
    }
    return render(request, 'dashboard/home.html', context)
