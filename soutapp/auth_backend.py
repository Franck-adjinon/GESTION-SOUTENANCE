from django.contrib.auth.backends import BaseBackend
from .models import Utilisateur  # Importer ton modèle personnalisé
from django.contrib.auth.hashers import check_password

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Utilisateur.objects.get(email=username)
            if check_password(password, user.password):  # Comparer le mot de passe
                return user
        except Utilisateur.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Utilisateur.objects.get(pk=user_id)
        except Utilisateur.DoesNotExist:
            return None
