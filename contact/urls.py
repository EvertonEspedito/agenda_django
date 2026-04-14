from django.urls import path
from . import views

urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact'),
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('sobre/', views.sobre, name='about'),
]