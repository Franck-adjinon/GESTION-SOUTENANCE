from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages # Import de Django messages frameworks pour afficher des messages de confirmation
# *Dans le cadre de la mise en place du processus d'authentification 
from django.urls import reverse_lazy 
from .forms import MessageForm, RegistrationForm, CustomAuthenticationForm, AdminAuthenticationForm
from .models import Message, Professeur, Soutenance, Utilisateur, administrateur 
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
# *Import generic views
from django.views.generic.detail import DetailView 
from django.views.generic import View
from django.utils.timezone import now 


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
            messages.success(request, 'Votre compte a été crée avec succès !')
            return redirect('login')  # Redirige vers la page de connexion
        else:
            messages.error(request, "Une erreur s'est produite. Veuillez vérifier le formulaire.")
    else:
        form = RegistrationForm()
    
    return render(request, 'session-templates/pages/create-account.html', {'form': form})


# TODO: Affiche le tableau de bord
def dashbord(request):
    
    # * Début gestion des utilisateurs
    """
    Puisque qu'on n'utilise pas le système de connexion de Django, vous devez manuellement vérifier si l'utilisateur est connecté dans vos autres vues
    """
    user_id = request.session.get('user_id')
    if not user_id: 
        return redirect('login') 
    # Récupérer l'utilisateur connecté pour en suite le passer à la page via {'user': user}
    user = Utilisateur.objects.get(id_user=user_id)
    # * Fin gestion des utilisateurs
    
    # compter le nombre de Soutenance terminer
    try:
        sout_finish = Soutenance.objects.filter(is_finish=True).count()
    except Exception as e:
        pass
    
    
    # Compter le nombre de soutenances non terminées
    try:
        sout_unfinish = Soutenance.objects.filter(is_finish=False).count()
    except Exception as e:
        pass
    
    
    # Récupérer toutes les soutenances non terminées avec leurs étudiants
    try:
        sout_etu = Soutenance.objects.filter(is_finish=False).select_related('id_etudiant').order_by('-created_at')
    except Exception as e:
        pass
    
    
    return render(request, 'session-templates/index.html', {'sout_finish': sout_finish, 'sout_unfinish': sout_unfinish, 'sout_etu': sout_etu, 'user': user})


# TODO: Affiche les soutenances prochaines sous forme de cards
def blog_next(request): 
    
    # * Début gestion des utilisateurs
    """
    Puisque qu'on n'utilise pas le système de connexion de Django, vous devez manuellement vérifier si l'utilisateur est connecté dans vos autres vues
    """
    user_id = request.session.get('user_id')
    if not user_id: 
        return redirect('login') 
    # Récupérer l'utilisateur connecté pour en suite le passer à la page via {'user': user}
    user = Utilisateur.objects.get(id_user=user_id)
    # * Fin gestion des utilisateurs
    
    
    # récupérer tout les non soutenances terminer
    try:
        sout = Soutenance.objects.filter(is_finish=False).select_related('id_etudiant__id_filiere').order_by('-created_at')
    except Exception as e:
        pass
    
    
    return render(request, 'session-blog/blog.html', {'sout': sout, 'user': user})


# TODO: Affiche les soutenances terminer sous forme de cards
def blog_past(request):
    
    # * Début gestion des utilisateurs
    """
    Puisque qu'on n'utilise pas le système de connexion de Django, vous devez manuellement vérifier si l'utilisateur est connecté dans vos autres vues
    """
    user_id = request.session.get('user_id')
    if not user_id: 
        return redirect('login') 
    # Récupérer l'utilisateur connecté pour en suite le passer à la page via {'user': user}
    user = Utilisateur.objects.get(id_user=user_id)
    # * Fin gestion des utilisateurs
    
    # récupérer tout les soutenances terminer
    try:
        sout_finish = Soutenance.objects.filter(is_finish=True).select_related('id_etudiant').order_by('-created_at')
    except Exception as e:
        pass
    
    
    return render(request, 'session-blog/blog.html', {'sout_finish': sout_finish, 'user': user})


# TODO: Affiche les informations d'une soutenance prochaine
class SoutDetail(DetailView):
    
    model = Soutenance
    template_name = 'session-blog/single.html'
    context_object_name = 'sout' 
    
    def dispatch(self, request, *args, **kwargs):
        # Vérifiez si l'utilisateur est connecté
        if not request.session.get('user_id'): 
            return redirect('login')
        
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Instance actuelle de Soutenance
        soutenance = self.object

        # Ajouter les détails à afficher dans le template
        context['sout_pre'] = soutenance  # Soutenance actuelle
        context['etudiant'] = soutenance.id_etudiant  # Étudiant associé
        context['filiere'] = soutenance.id_etudiant.id_filiere  # Filière de l'étudiant

        # Professeurs supervisant cette soutenance
        try:
            context['superviseurs'] = soutenance.superviser_set.all().order_by('-created_at')
        except Exception as e:
            pass
        
        # Images banniere
        try:
            context['soutenance_banniere'] = soutenance.soutenanceimage_set.filter(pour="banniere").first()
        except Exception as e:
            pass

        # Rapport lié à cette soutenance
        try:
            context['rapport'] = soutenance.rapport_set.first()
        except Exception as e:
            pass
        

        # Appréciations des professeurs
        try :
            context['appreciations'] = soutenance.apprecier_set.all().order_by('-create_at')
        except Exception as e:
            pass

        # Soutenances non terminées
        try:
            context['soutenances_non_terminees'] = Soutenance.objects.filter(is_finish=False).order_by('-created_at')
        except Exception as e:
            pass
        

        return context


# TODO: Affiche les informations d'une soutenance terminer
class SoutDetailFinish(DetailView):
    model = Soutenance
    template_name = 'session-blog/single.html'
    context_object_name = 'soutfinish' 
    
    def dispatch(self, request, *args, **kwargs):
        # Vérifiez si l'utilisateur est connecté
        if not request.session.get('user_id'): 
            return redirect('login')
        
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Instance actuelle de Soutenance
        soutenance = self.object

        # Ajouter les détails à afficher dans le template
        context['sout_pre'] = soutenance  # Soutenance actuelle
        context['etudiant'] = soutenance.id_etudiant  # Étudiant associé
        context['filiere'] = soutenance.id_etudiant.id_filiere  # Filière de l'étudiant

        # Professeurs supervisant cette soutenance
        try:
            context['superviseurs'] = soutenance.superviser_set.all().order_by('-created_at')
        except Exception as e:
            pass
        

        # Images associées à cette soutenance
        try:
            context['soutenance_images'] = soutenance.soutenanceimage_set.filter(pour="rapport")
        except Exception as e:
            pass
        

        # Images banniere
        try:
            context['soutenance_banniere'] = soutenance.soutenanceimage_set.filter(pour="banniere").first()
        except Exception as e:
            pass
        

        # Rapport lié à cette soutenance
        try: 
            context['rapport'] = soutenance.rapport_set.last()
        except Exception as e:
            pass
        

        # Appréciations des professeurs
        try:
            context['appreciations'] = soutenance.apprecier_set.all().order_by('-created_at')
        except Exception as e:
            pass
        

        # Soutenances non terminées
        try:
            context['soutenances_non_terminees'] = Soutenance.objects.filter(is_finish=False).order_by('-created_at')
        except Exception as e:
            pass
        

        return context


# TODO: Affiche les Détails d'un professeur
class ProfDetail(DetailView):
    model = Professeur
    template_name = 'session-blog/prof_detail.html'
    context_object_name = 'prof' 
    
    def dispatch(self, request, *args, **kwargs):
        # Vérifiez si l'utilisateur est connecté
        if not request.session.get('user_id'): 
            return redirect('login')
        
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Instance actuelle de Soutenance
        professeur = self.object

        # Ajouter les détails à afficher dans le template
        context['prof_pre'] = professeur  # professeur actuelle
        try:
            context['lien'] = professeur.liensociale_set.all()  # lien associé
        except Exception as e:
            pass
        

        return context


# TODO: Gère l'envoie des messages de l'utilisateur
def contact(request):
    
    # * Début gestion des utilisateurs
    """
    Puisque qu'on n'utilise pas le système de connexion de Django, vous devez manuellement vérifier si l'utilisateur est connecté dans vos autres vues
    """
    user_id = request.session.get('user_id')
    if not user_id: 
        return redirect('login') 
    # Récupérer l'utilisateur connecté pour en suite le passer à la page via {'user': user}
    user = Utilisateur.objects.get(id_user=user_id)
    # * Fin gestion des utilisateurs
    
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
            form = MessageForm()  # Réinitialiser le formulaire après soumission
        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')
    
    return render(request, 'session-blog/contact.html', {'form': form, 'user': user})


# TODO: Affiche la section faq
def faq(request):
    
    # * Début gestion des utilisateurs
    """
    Puisque qu'on n'utilise pas le système de connexion de Django, vous devez manuellement vérifier si l'utilisateur est connecté dans vos autres vues
    """
    user_id = request.session.get('user_id')
    if not user_id: 
        return redirect('login') 
    # Récupérer l'utilisateur connecté pour en suite le passer à la page via {'user': user}
    user = Utilisateur.objects.get(id_user=user_id)
    # * Fin gestion des utilisateurs
    
    return render(request, 'session-blog/faq.html', {'user': user})


# TODO: Affiche les professeurs
def prof(request):
    
    # * Début gestion des utilisateurs
    """
    Puisque qu'on n'utilise pas le système de connexion de Django, vous devez manuellement vérifier si l'utilisateur est connecté dans vos autres vues
    """
    user_id = request.session.get('user_id')
    if not user_id: 
        return redirect('login') 
    # Récupérer l'utilisateur connecté pour en suite le passer à la page via {'user': user}
    user = Utilisateur.objects.get(id_user=user_id)
    # * Fin gestion des utilisateurs
    
    # *Récupérer tout les prof
    try:
        prof = Professeur.objects.all().order_by('-created_at')
    except Exception as e:
        pass
    
    return render(request, 'session-blog/prof.html', {'prof': prof, 'user': user})


# TODO: Fonction pour gérer la déconnexion 
def logout_view(request):
    if 'user_id' in request.session:
        del request.session['user_id']  # Supprimer l'utilisateur de la session 
    return redirect('login')


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
            
            try:
                # Vérifier si l'utilisateur existe dans la base de données
                user = Utilisateur.objects.get(email=email)
                if check_password(password, user.password):  # Vérifier le mot de passe
                    # Simuler la connexion de l'utilisateur
                    request.session['user_id'] = user.id_user  # Stocker l'ID utilisateur dans la session
                    user.last_login = now()
                    user.save()
                    messages.success(request, "Connexion réussie !")
                    return redirect(self.success_url)
                else:
                    messages.error(request, "Mot de passe incorrect.")
            except Utilisateur.DoesNotExist:
                messages.error(request, "Cet email n'est pas enregistré.")
        else:
            messages.error(request, "Veuillez vérifier vos informations.")

        return render(request, self.template_name, {'form': form})


# TODO:  Afficher l'interface de connexion des administrateurs
class login_admin(View):
    template_name = 'session-admin/pages/login.html'
    success_url = reverse_lazy('admin-dashboard')  # Redirection après connexion réussie

    def get(self, request):
        form = AdminAuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AdminAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                # Vérifier si l'administrateur existe dans la base de données
                user = administrateur.objects.get(email=email)
                if password == user.password:  # Vérifier le mot de passe
                    # Simuler la connexion de l'administrateur
                    request.session['user_id'] = user.id_admin  # Stocker l'ID administrateur dans la session
                    user.last_login = now()
                    user.save()
                    messages.success(request, "Connexion réussie !")
                    return redirect(self.success_url)
                else:
                    messages.error(request, "Mot de passe incorrect.")
            except administrateur.DoesNotExist:
                messages.error(request, "Cet email n'est pas enregistré.")
        else:
            messages.error(request, "Veuillez vérifier vos informations.")
    
        return render(request, self.template_name, {'form': form})


# TODO:  Affiche le tableau de bord des administrateurs
def admin_dashboard(request):
    
    # * Début gestion des administrateur 
    user_id = request.session.get('user_id')
    if not user_id: 
        return redirect('login') 
    # Récupérer l'administrateur connecté pour en suite le passer à la page via {'user': user}
    user = administrateur.objects.get(id_admin=user_id)
    # * Fin gestion des administrateur
    
    # compter le nombre de Soutenance terminer
    try:
        sout_finish = Soutenance.objects.filter(is_finish=True).count()
    except Exception as e:
        pass
    
    
    # Compter le nombre de soutenances non terminées
    try:
        sout_unfinish = Soutenance.objects.filter(is_finish=False).count()
    except Exception as e:
        pass
    
    
    # Récupérer toutes les soutenances non terminées avec leurs étudiants
    try:
        sout_etu = Soutenance.objects.filter(is_finish=False).select_related('id_etudiant').order_by('-created_at')
    except Exception as e:
        pass
    
    
    return render(request, 'session-admin/dashboard.html', {'sout_finish': sout_finish, 'sout_unfinish': sout_unfinish, 'sout_etu': sout_etu, 'user': user})


# TODO:  Fonction pour gérer la déconnexion des administrateurs
def logout_admin_view(request):
    if 'user_id' in request.session:
        del request.session['user_id']  # Supprimer l'utilisateur de la session 
    return redirect('administrateur')


# TODO: Fonction pour afficher le profil de l'admin
def profil_admin(request):
    
    
    # * Début gestion des administrateur 
    user_id = request.session.get('user_id')
    if not user_id: 
        return redirect('login') 
    # Récupérer l'administrateur connecté pour en suite le passer à la page via {'user': user}
    user = administrateur.objects.get(id_admin=user_id)
    # * Fin gestion des administrateur
    
    # *Gestion du formulaire
    use = get_object_or_404(administrateur, id_admin=user_id)
    if request.method == 'POST':
        try:  
            
            use.nom_admin=request.POST.get('nom_user', use.nom_admin)
            use.prenom_admin=request.POST.get('prenom_user', use.prenom_admin)
            use.email=request.POST.get('email_user', use.email)
            use.password=request.POST.get('password_user', use.password)
            
            # contrôle des champs vides 
            if use.nom_admin == '':
                use.nom_admin = user.nom_admin
            if use.prenom_admin == '':
                use.prenom_admin = user.prenom_admin
            if use.email == '':
                use.email = user.email
            if use.password == '':
                use.password = user.password
            
            use.save() 
            
            # Récupérer les informations mis à jour de l'admin 
            user = administrateur.objects.get(id_admin=user_id)
            
            return redirect('profil_admin', {'user': user})  
        except Exception as e:
            return render(request, 'session-admin/profil.html', {'error': f"Erreur lors de la mise à jour : {str(e)}", 'user': user})
        
    
    return render(request, 'session-admin/profil.html', {'user': user})


# TODO: Fonction pour afficher le profil de l'utilisateur
def user_profil(request):
    
    # * Début gestion des utilisateurs
    user_id = request.session.get('user_id')
    if not user_id: 
        return redirect('login') 
    # Récupérer l'utilisateur connecté pour en suite le passer à la page via {'user': user}
    user = Utilisateur.objects.get(id_user=user_id)
    # * Fin gestion des utilisateurs
    
    
    # *Gestion du formulaire
    use = get_object_or_404(Utilisateur, id_user=user_id)
    if request.method == 'POST':
        try:  
            
            use.nom_user=request.POST.get('nom_user', use.nom_user)
            use.prenom_user=request.POST.get('prenom_user', use.prenom_user)
            use.email=request.POST.get('email_user', use.email)
            use.password=request.POST.get('password_user', use.password)
            
            #hacher le mot de passe
            correct_password = use.password
            hach_password = make_password(correct_password)
            use.password = hach_password
            
            # contrôle des champs vides 
            if use.nom_user == '':
                use.nom_user = user.nom_user
            if use.prenom_user == '':
                use.prenom_user = user.prenom_user
            if use.email == '':
                use.email = user.email
            if use.password == '':
                use.password = user.password
            
            use.save() 
            
            # Récupérer les informations mis à jour de l'utilisateur 
            user = Utilisateur.objects.get(id_user=user_id)
            
            return redirect('user_profil', {'user': user})  
        except Exception as e:
            return render(request, 'session-blog/user_profil.html', {'error': f"Erreur lors de la mise à jour : {str(e)}", 'user': user})
        
    
    return render(request, 'session-blog/user_profil.html', {'user': user})