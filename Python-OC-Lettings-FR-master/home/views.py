from django.shortcuts import render


# Vue pour la page d'accueil
def index(request):
    return render(request, 'index.html')


# Vue pour la page d'erreur 404
def page_not_found(request, exception):
    return render(request, '404.html', status=404)
