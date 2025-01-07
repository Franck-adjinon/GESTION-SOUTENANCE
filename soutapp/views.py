from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#Dans le cadre de la mise en place du processus d'authentification
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import RegistrationForm, MessageForm, CustomAuthenticationForm
from django.contrib import messages # Import de Django messages frameworks pour afficher des messages de confirmation
from .models import Message, Utilisateur, Professeur, Soutenance
# TODO: Import generic views
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.utils.timezone import now
from django.views.generic import FormView
from .forms import UpdateUserInfo


# TODO: Affiche l'accueil du site qui est en même temps la page d'inscription
def index(request): 
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Hachage du mot de passe avant de l'enregistrer
            password_hache = make_password(form.cleaned_data['password'])
            
            Utilisateur.objects.create(
                nom_user=form.cleaned_data['nom_user'],
                prenom_user=form.cleaned_data['prenom_user'],
                email=form.cleaned_data['email'],
                password=password_hache,
            )
            #messages.success(request, 'Votre compte a été crée avec succès !')
            return redirect('login')  # Redirige vers la page de connexion
        else:
            messages.error(request, "Une erreur s'est produite. Veuillez vérifier le formulaire.")
    else:
        form = RegistrationForm()

    return render(request, 'session-templates/pages/create-account.html', {'form': form})


# TODO: Affiche le tableau de bord
@login_required
def dashbord(request):
    # compter le nombre de Soutenance terminer
    sout_finish = Soutenance.objects.filter(is_finish=True).count()
    
    # Compter le nombre de soutenances non terminées
    sout_unfinish = Soutenance.objects.filter(is_finish=False).count()
    
    # Récupérer toutes les soutenances non terminées avec leurs étudiants
    sout_etu = Soutenance.objects.filter(is_finish=False).select_related('id_etudiant')
    
    return render(request, 'session-templates/index.html', {'sout_finish': sout_finish, 'sout_unfinish': sout_unfinish, 'sout_etu': sout_etu})


# TODO: Affiche les soutenances prochaines sous forme de cards
@login_required
def blog_next(request): 
    # récupérer tout les soutenances terminer
    sout = Soutenance.objects.filter(is_finish=False).select_related('id_etudiant__id_filiere')
    
    return render(request, 'session-blog/blog.html', {'sout': sout})


# TODO: Affiche les soutenances terminer sous forme de cards
@login_required
def blog_past(request):
    # récupérer tout les soutenances terminer
    sout_finish = Soutenance.objects.filter(is_finish=True).select_related('id_etudiant')
    
    return render(request, 'session-blog/blog.html', {'sout_finish': sout_finish})


# TODO: Affiche les informations d'une soutenance prochaine
class SoutDetail(LoginRequiredMixin, DetailView):
    model = Soutenance
    template_name = 'session-blog/single.html'
    context_object_name = 'sout' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Instance actuelle de Soutenance
        soutenance = self.object

        # Ajouter les détails à afficher dans le template
        context['sout_pre'] = soutenance  # Soutenance actuelle
        context['etudiant'] = soutenance.id_etudiant  # Étudiant associé
        context['filiere'] = soutenance.id_etudiant.id_filiere  # Filière de l'étudiant

        # Professeurs supervisant cette soutenance
        context['superviseurs'] = soutenance.superviser_set.all()

        # Images associées à cette soutenance
        context['soutenance_images'] = soutenance.soutenanceimage_set.all()

        # Images banniere
        context['soutenance_banniere'] = soutenance.soutenanceimage_set.filter(pour="banniere").first()

        # Rapport lié à cette soutenance
        context['rapport'] = soutenance.rapport_set.first()

        # Appréciations des professeurs
        context['appreciations'] = soutenance.apprecier_set.all()

        # Soutenances non terminées
        context['soutenances_non_terminees'] = Soutenance.objects.filter(is_finish=False)

        return context


# TODO: Affiche les informations d'une soutenance terminer
class SoutDetailFinish(LoginRequiredMixin, DetailView):
    model = Soutenance
    template_name = 'session-blog/single.html'
    context_object_name = 'soutfinish' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Instance actuelle de Soutenance
        soutenance = self.object

        # Ajouter les détails à afficher dans le template
        context['sout_pre'] = soutenance  # Soutenance actuelle
        context['etudiant'] = soutenance.id_etudiant  # Étudiant associé
        context['filiere'] = soutenance.id_etudiant.id_filiere  # Filière de l'étudiant

        # Professeurs supervisant cette soutenance
        context['superviseurs'] = soutenance.superviser_set.all()

        # Images associées à cette soutenance
        context['soutenance_images'] = soutenance.soutenanceimage_set.filter(pour="rapport")

        # Images banniere
        context['soutenance_banniere'] = soutenance.soutenanceimage_set.filter(pour="banniere").first()

        # Rapport lié à cette soutenance
        context['rapport'] = soutenance.rapport_set.first()

        # Appréciations des professeurs
        context['appreciations'] = soutenance.apprecier_set.all()

        # Soutenances non terminées
        context['soutenances_non_terminees'] = Soutenance.objects.filter(is_finish=False)

        return context


# TODO: Affiche les Détails d'un professeur
class ProfDetail(LoginRequiredMixin, DetailView):
    model = Professeur
    template_name = 'session-blog/prof_detail.html'
    context_object_name = 'prof' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Instance actuelle de Soutenance
        professeur = self.object

        # Ajouter les détails à afficher dans le template
        context['prof_pre'] = professeur  # professeur actuelle
        context['lien'] = professeur.liensociale_set.all()  # lien associé

        return context


# TODO: Affiche et la mise à jour des informations de l'utilisateur connecter
class UserDetail(LoginRequiredMixin, DetailView):
    model = Utilisateur
    template_name = 'session-blog/user_profil.html'
    form_class = UpdateUserInfo
    success_url = reverse_lazy('user_profil')  # Rediriger après mise à jour
    
    """
    def get_initial(self):
        #Pré-remplir les champs avec les données actuelles de l'utilisateur.
        utilisateur = get_object_or_404(Utilisateur, pk=self.kwargs['pk'])
        return {
            'nom_user': utilisateur.nom_user,
            'prenom_user': utilisateur.prenom_user,
            'email': utilisateur.email,
            'password': utilisateur.password,
        }
    """
    
    def form_valid(self, form):
        """Enregistrer les modifications apportées à l'utilisateur."""
        utilisateur = get_object_or_404(Utilisateur, pk=self.kwargs['pk'])

        # Mettre à jour les champs de l'utilisateur
        utilisateur.nom_user = form.cleaned_data['nom_user']
        utilisateur.prenom_user = form.cleaned_data['prenom_user']
        utilisateur.email = form.cleaned_data['email']
        if form.cleaned_data['password']:
            utilisateur.set_password(form.cleaned_data['password'])  # Hachage du mot de passe

        utilisateur.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        """Ajouter les détails supplémentaires au contexte."""
        context = super().get_context_data(**kwargs)
        utilisateur = get_object_or_404(Utilisateur, pk=self.kwargs['pk'])
        
        # Pré-remplir le formulaire avec les données de l'utilisateur
        form = UpdateUserInfo(initial={
            'nom_user': utilisateur.nom_user,
            'prenom_user': utilisateur.prenom_user,
            'email': utilisateur.email,
        })

        context['form'] = form
        context['user_pre'] = utilisateur
        return context


# TODO: Gère l'envoie des messages de l'utilisateur
@login_required
def contact(request):
    # *Gestion du formulaire
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Sauvegarder les données du formulaire
            Message.objects.create(
                sujet=form.cleaned_data['sujet'],
                email_user=form.cleaned_data['email_user'],
                message=form.cleaned_data['message'],
            )
            messages.success(request, 'Votre message a été envoyé avec succès !')
            form = MessageForm()  # Réinitialiser le formulaire après soumission
        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')
    
    return render(request, 'session-blog/contact.html', {'form': form})


# TODO: Affiche la section faq
@login_required
def faq(request):
    return render(request, 'session-blog/faq.html')


# TODO: Affiche les professeurs
@login_required
def prof(request):
    # *Récupérer tout les prof
    prof = Professeur.objects.all() 
    
    return render(request, 'session-blog/prof.html', {'prof': prof})

"""
@login_required
def prof_detail(request):
    return render(request, 'session-blog/prof_detail.html')
"""


@login_required
def user_profil(request):
    return render(request, 'session-blog/user_profil.html')

# TODO: Class pour gérer la connexion
class CustomLoginView(View):
    template_name = 'session-templates/pages/login.html'
    success_url = reverse_lazy('dashbord')  # Redirection après connexion réussie

    def get(self, request):
        form = CustomAuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Authentification
            user = authenticate(request, username=email, password=password)
            if user is not None:
                # Mettre à jour last_login
                user.last_login = now()
                user.save()
                login(request, user)
                return redirect(self.success_url)
            else:
                messages.error(request, "Identifiants incorrects.")
        else:
            messages.error(request, "Veuillez vérifier vos informations.")

        return render(request, self.template_name, {'form': form})

# TODO: Fonction pour gérer la déconnexion 
def logout_view(request):
    logout(request)
    return redirect('login')