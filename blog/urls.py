from django.urls import path

from . import views
urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('article/<int:id>-<slug:slug>', views.lire, name='lire'),
    path('redirection',views.view_redirection,name="rd"),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition)
]
