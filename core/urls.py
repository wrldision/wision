from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import (
    ajout_besoin,
    home_view,
    apropos,
    thankyou,
    BesoinListView,
    BesoinDetailView,
    ajout_don,
    )

app_name = 'core'

urlpatterns =[
    path('', home_view, name='home'),
    path('besoin/', BesoinListView.as_view(), name='liste'),
    path('besoin/<int:pk>/', BesoinDetailView.as_view(), name='detail'),
    path('ajoutbesoin/', ajout_besoin, name='ajouter_besoin'),
    path('ajoutdon/', ajout_don, name='ajouter_don'),
    path('toulesdons/', ajout_don, name='listedesdon'),
    path('apropos/', apropos, name='apropos'),
    path('thankyou/', thankyou, name='thankyou'),
]