# Module de tests pour l'application Home.
from django.test import TestCase
from django.urls import reverse


class HomeTest(TestCase):
    # Classe de tests pour les vues de l'application Home.

    def test_index(self):
        # Teste la vue 'home:index'.
        response = self.client.get(reverse('home:index'))
        assert response.status_code == 200
        assert b"<title>Holiday Homes</title>" in response.content
