from django.urls import path
from . import views

urlpatterns = [
    path('contacts/<int:contact_id>/detail/', views.contact, name='contact'),
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('contacts/create/', views.create, name='create'),
    path('sobre/', views.sobre, name='about'),
]