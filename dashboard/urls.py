from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import (
    home_view,
    )

app_name = 'dashboard'

urlpatterns =[
    path('', home_view, name='home'),
    
]