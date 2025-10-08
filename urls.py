from django.urls import path
from . import views

urlpatterns = [
    path('', views.land, name="land"),
    path('signin', views.signin, name="signin"),
    path('mylogin', views.mylogin, name="mylogin"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('about/', views.about, name="about"),
    path('cases', views.cases, name="cases"),
    path('profile', views.profile, name="profile"),
    path('adoption/', views.adoption, name="adoption"),
    path('lost-pets/', views.lostpets, name="lostpets"),
    path('events/', views.events, name="events"),
    path('wset/', views.wset, name="wset"),
    path('base/', views.base, name="base"),
    path('logouts/', views.logouts, name="logouts"),
]