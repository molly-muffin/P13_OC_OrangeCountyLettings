# Module de tests pour l'application Lettings.
from django.test import TestCase
from django.urls import reverse
from .models import Address, Letting


class LettingsTest(TestCase):
    # Classe de tests pour les vues et les modèles de Lettings.

    def test_lettings_index(self):
        # Teste la vue 'lettings:index'.
        response = self.client.get(reverse('lettings:index'))
        assert response.status_code == 200
        assert b"<title>Lettings</title>" in response.content

    def setUp(self):
        # Initialise les données pour les tests.
        self.address = Address.objects.create(number=1,
                                              street="StreetTest",
                                              city="CityTest",
                                              state="StateTest",
                                              zip_code=00000,
                                              country_iso_code="FRA")
        self.letting = Letting.objects.create(title="Letting Test", address=self.address)

    def test_letting_detail(self):
        # Teste la vue 'lettings:letting'.
        response = self.client.get(reverse('lettings:letting', args=[1]))
        assert response.status_code == 200
        assert b"<title>Letting Test</title>" in response.content

    def test_address_model(self):
        # Teste la méthode __str__ de l'objet Address.
        assert str(self.address) == f'{self.address.number} {self.address.street}'

    def test_letting_model(self):
        # Teste la méthode __str__ de l'objet Letting.
        assert str(self.letting) == self.letting.title
