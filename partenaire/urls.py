from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import (
    ajout_partenaire,
    PartenaireListView,
    PartenaireDetailView,
    )

app_name = 'partenaire'

urlpatterns =[
    #path('', home_view, name='home'),
    path('partner/', PartenaireListView.as_view(), name='liste'),
    path('partner/<int:pk>/', PartenaireDetailView.as_view(), name='detail'),
    path('ajoutpartner/', ajout_partenaire, name='ajouter_partenaire'),
]