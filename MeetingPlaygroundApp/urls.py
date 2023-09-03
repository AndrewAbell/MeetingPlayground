
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name='index'),
    path('newsletter/', views.newsletter ,name='newsletter'),
    path('pricing/', views.pricing ,name='pricing'),
    path('resources/', views.resources ,name='resources'),
    path('signup/', views.signup ,name='signup'),
    path('Game/', views.Game ,name='Game'),
    path('GameTwo/', views.GameTwo ,name='GameTwo'),
    path('GameThree/', views.GameThree ,name='GameThree'),
    path('GameFour/', views.GameFour ,name='GameFour'),
    path('GameFive/', views.GameFive ,name='GameFive'),
    path('GameSix/', views.GameSix ,name='GameSix'),
]

