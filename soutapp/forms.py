from django import forms  
from .models import Utilisateur, administrateur
from django.contrib.auth.hashers import check_password


# Formulaire pour l'envoie de message
class MessageForm(forms.Form):
    sujet = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Sujet'
    }))
    email_user = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Votre Email'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'message',
        'rows': 7,
        'cols': 30,
        'placeholder': 'Message'
    }))


# Formulaire pour l'authentification
class CustomAuthenticationForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'autofocus': True,
        'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
        'placeholder': 'Votre Adresse mail'
    }))
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={
        'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
        'placeholder': 'Mots de Passe'
    }))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        # Vérifie si les informations sont valides dans la base de données
        try:
            user = Utilisateur.objects.get(email=email)
            if not check_password(password, user.password):  # Utilisation de check_password
                raise forms.ValidationError("Mot de passe incorrect.")
        except Utilisateur.DoesNotExist:
            raise forms.ValidationError("Cet email n'est pas enregistré.")

        return cleaned_data


# Formulaire pour la création de compte
class RegistrationForm(forms.Form):
    nom_user = forms.CharField(label="Nom", max_length=200, widget=forms.TextInput(attrs={
        'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
        'id': 'lname',
        'placeholder': 'Votre nom'
    }))
    prenom_user = forms.CharField(label="Prénom", max_length=200, widget=forms.TextInput(attrs={
        'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
        'id': 'fname',
        'placeholder': 'Votre prenom'
    }))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
        'id': 'email',
        'placeholder': 'Adresse Email'
    }))
    password = forms.CharField(label="Mots de Passe", max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
        'id': 'password',
        'placeholder': 'Mots de Passe'
    }))
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Utilisateur.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email est déjà utilisé.")
        return email


# Formulaire pour l'authentification des administrateurs
class AdminAuthenticationForm(forms.Form):
    email = forms.EmailField(label='Email Admin', widget=forms.EmailInput(attrs={
        'autofocus': True,
        'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
        'placeholder': 'Votre Adresse mail'
    }))
    password = forms.CharField(label='Mot de passe Admin', widget=forms.PasswordInput(attrs={
        'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
        'placeholder': 'Mots de Passe'
    }))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        # Vérifie si les informations sont valides dans la base de données
        try:
            user = administrateur.objects.get(email=email)
            if not password == user.password:  
                raise forms.ValidationError("Mot de passe incorrect.")
        except administrateur.DoesNotExist:
            raise forms.ValidationError("Cet email n'est pas enregistré.")

        return cleaned_data