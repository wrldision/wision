from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from .models import Don, Besoin
from .forms import DonForm, BesoinForm
from partenaire.models import Partenaire


# Create your views here.
def home_view(request):
    PartenaireQueryLatest = None
    BesoinQueryLatest = None
    DonQueryLatest = None

    BesoinQueryLatest = Besoin.objects.all().order_by('-created_at')[:3] #Les 03 Derniers Besoins
    DonQueryLatest = Don.objects.all().order_by('-created_at')[:6] #Les 06 Derniers Dons
    PartenaireQueryLatest = Partenaire.objects.all().order_by('-created_at')[:4] #Les 04 Derniers Besoins

    # Nombre de personne ayant visiter la page d'acceuil
    nbr_visiteurs = request.session.get('nbr_visiteurs', 0)
    request.session['nbr_visiteurs'] = nbr_visiteurs + 1

    context = {
        'BesoinQueryLatest':BesoinQueryLatest,
        'DonQueryLatest':DonQueryLatest,
        'PartenaireQueryLatest':PartenaireQueryLatest,
        'nbr_visiteurs': nbr_visiteurs, #ToDo
        #'':,
    }
    return render(request, 'core/home.html', context)


def ajout_besoin(request):
    form = BesoinForm(request.POST or None)
    # A HTTP Post?
    if request.method == 'POST':
        # Le formulaire est-il valide?
        print("....Tring")
        if form:
            form.save()
            print("...is done")
            #redirection si tout se passe bien
            return redirect('/')
        else:
            # Si Formulaire contient erreur 
            print("...requete != valid")
            return render(request, 'core/ajout-besoin.html', {'form':form})
    print("...requete != POST")    
    return render(request, 'core/ajout-besoin.html', {'form':form})

def ajout_don(request):
    form = DonForm(request.POST or None)
    # A HTTP Post?
    if request.method == 'POST':
        # Le formulaire est-il valide?
        print("....Tring")
        if form:
            form.save()
            print("...is done")
            #redirection si tout se passe bien
            return redirect('/thankyou')
        else:
            # Si Formulaire contient erreur 
            print("...requete != valid")
            return render(request, 'core/ajout-don.html', {'form':form})
    print("...requete != POST")    
    return render(request, 'core/ajout-don.html', {'form':form})

def apropos(request):
    team_message = ""
    return render(request, 'core/apropos.html', {'message':team_message})

def thankyou(request):
    team_message = ""
    return render(request, 'core/thankyou.html', {'message':team_message})


class BesoinListView(ListView):
    model = Besoin
    template_name = 'core/besoin-list.html'
    context_object_name = 'besoin' # the default name is 'object_list'

class BesoinDetailView(DetailView):
    model = Besoin
    template_name = 'core/besoin-detail.html'

class DonListView(ListView):
    model = Don
    template_name = 'core/don-list.html'
    context_object_name = 'don' # the default name is 'object_list'

