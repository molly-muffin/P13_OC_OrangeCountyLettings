from django.urls import path
from .views import index


# Namespace pour les URLs de l'application 'home'
app_name = 'home'

urlpatterns = [
    # URL de la page d'accueil
    path('', index, name='index'),
]
