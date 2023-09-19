from django.shortcuts import render


# Vue pour la page d'accueil
def index(request):
    return render(request, 'index.html')
