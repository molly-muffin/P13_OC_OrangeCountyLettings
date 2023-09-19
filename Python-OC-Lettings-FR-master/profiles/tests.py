# Module de tests pour l'application Profiles.
from django.test import TestCase
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


class ProfilesTest(TestCase):
    # Classe de tests pour les vues et les modèles de Profiles.

    def test_profiles_index(self):
        # Teste la vue 'profiles:index'.
        response = self.client.get(reverse('profiles:index'))
        assert response.status_code == 200
        assert b"<title>Profiles</title>" in response.content

    def setUp(self):
        # nitialise les données pour les tests.
        self.user = User.objects.create_user(username="Username",
                                             password="PasswordForUsername",
                                             email="Username@gmail.com")
        self.profile = Profile.objects.create(user=self.user, favorite_city="CityTest")

    def test_profile_detail(self):
        # Teste la vue 'profiles:profile'.
        response = self.client.get(reverse('profiles:profile', args=["Username"]))
        assert response.status_code == 200
        assert b"<title>Username</title>" in response.content

    def test_profile_model(self):
        # Teste la méthode __str__ de l'objet Profile.
        assert str(self.profile) == self.user.username
