from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from .models import Partenaire
from .forms import PartenaireForm
# Create your views here.

# def home_view(request):
#     PartenaireQueryAll = Partenaire.objects.all().order_by('-created_at')[:9] #.order_by() du plus récent au moins récent.
#     context = {
#         "PartenaireQueryAll": PartenaireQueryAll
#     }
#     message = "hello"
#     return render(request, 'core/partner.html',{"PartenaireQueryAll": PartenaireQueryAll})



def ajout_partenaire(request):
    form = PartenaireForm(request.POST or None)
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
            return render(request, 'participant/ajout.html', {'form':form})
    print("...requete != POST")    
    return render(request, 'partenaire/ajout.html', {'form':form})



class PartenaireListView(ListView):
    model = Partenaire
    template_name = 'partenaire/list.html'
    context_object_name = 'Partner' # the default name is 'object_list'



class PartenaireDetailView(DetailView):
    model = Partenaire
    template_name = 'partenaire/detail.html'