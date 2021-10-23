from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import (
    home_view,
    PartenaireListView,
    PartenaireDetailView,
    )

app_name = 'partenaire'

urlpatterns =[
    path('', home_view, name='home'),
    path('partner/', PartenaireListView.as_view(), name='liste'),
    path('partner/<int:pk>/', PartenaireDetailView.as_view(), name='detail'),
]