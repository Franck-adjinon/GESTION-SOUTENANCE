from django.shortcuts import render, get_object_or_404, redirect
from .models import Superviser, Apprecier, administrateur, LienSociale, Professeur, Rapport, Soutenance, Filiere, Etudiant, Photo, SoutenanceImage










# --- Superviser CRUD Operations ---
def list_supervisers(request):
    # * Début gestion des administrateur 
    user_id = request.session.get('user_id')
    if not user_id: 
        return redirect('login') 
    # Récupérer l'administrateur connecté pour en suite le passer à la page via {'user': user}
    user = administrateur.objects.get(id_admin=user_id)
    # * Fin gestion des administrateur
    
    if request.method == 'GET':
        supervisers = Superviser.objects.all()
        return render(request, 'session-admin/list.html', {'supervisers': supervisers})


def create_superviser(request):
    if request.method == 'POST':
        try:
            id_sout = request.POST.get('id_sout')
            id_prof = request.POST.get('id_prof')
            role = request.POST.get('role')

            Superviser.objects.create(
                id_sout_id=id_sout,
                id_prof_id=id_prof,
                role=role
            )
            return redirect('list_supervisers')  # Redirige vers la liste après la création
        except Exception as e:
            return render(request, 'session-admin/form_gestion.html', {'error': f"Erreur lors de la création : {str(e)}"})

    Soutenances = Soutenance.objects.all()
    Professeurs = Professeur.objects.all()
    return render(request, 'session-admin/form_gestion.html', {'view_name': 'create_superviser', 'Professeurs': Professeurs, 'Soutenances': Soutenances})  # Page de formulaire pour créer


def update_superviser(request, id):
    superviser = get_object_or_404(Superviser, id=id)
    if request.method == 'POST':
        try:
            superviser.role = request.POST.get('role', superviser.role)
            superviser.save()
            return redirect('list_supervisers')  # Redirige vers la liste après la mise à jour
        except Exception as e:
            return render(request, 'supervisers/update.html', {'error': f"Erreur lors de la mise à jour : {str(e)}", 'superviser': superviser})

    return render(request, 'supervisers/update.html', {'superviser': superviser})  # Page de formulaire pour modifier


def delete_superviser(request, id_prof, id_sout, create_at):
    try:
        # Convertir la date en objet datetime pour la recherche
        from datetime import datetime
        create_at_parsed = datetime.strptime(create_at, '%Y-%m-%dT%H:%M:%S')

        # Récupérer l'objet Superviser
        superviser = get_object_or_404(
            Superviser,
            id_prof__id=id_prof,
            id_sout__id=id_sout,
            create_at=create_at_parsed
        ) 
        
        if request.method == 'POST':
            superviser.delete()
            return redirect('list_supervisers')

        return render(request, 'supervisers/delete.html', {'superviser': superviser})

    except Exception as e:
        return render(request, 'supervisers/delete.html', {
            'error': f"Erreur lors de la suppression : {str(e)}"
        })


# --- Apprecier CRUD Operations ---
def list_apprecies(request):
    if request.method == 'GET':
        apprecies = Apprecier.objects.all()
        return render(request, 'session-admin/list.html', {'apprecies': apprecies})


def create_apprecier(request):
    if request.method == 'POST':
        try:
            id_sout = request.POST.get('id_sout')
            id_prof = request.POST.get('id_prof')
            appreciation = request.POST.get('appreciation')

            Apprecier.objects.create(
                id_sout_id=id_sout,
                id_prof_id=id_prof,
                appreciation=appreciation
            )
            return redirect('list_apprecies')  # Redirige vers la liste après la création
        except Exception as e:
            return render(request, 'session-admin/form_gestion.html', {'error': f"Erreur lors de la création : {str(e)}", 'view_name': 'create_apprecier'})

    Soutenances = Soutenance.objects.all()
    Professeurs = Professeur.objects.all()
    return render(request, 'session-admin/form_gestion.html', {'view_name': 'create_apprecier', 'Professeurs': Professeurs, 'Soutenances': Soutenances})  # Page de formulaire pour créer


def update_apprecier(request, id):
    apprecier = get_object_or_404(Apprecier, id=id)
    if request.method == 'POST':
        try:
            apprecier.appreciation = request.POST.get('appreciation', apprecier.appreciation)
            apprecier.save()
            return redirect('list_apprecies')  # Redirige vers la liste après la mise à jour
        except Exception as e:
            return render(request, 'apprecies/update.html', {'error': f"Erreur lors de la mise à jour : {str(e)}", 'apprecier': apprecier})

    return render(request, 'apprecies/update.html', {'apprecier': apprecier})  # Page de formulaire pour modifier


def delete_apprecier(request, id):
    apprecier = get_object_or_404(Apprecier, id=id)
    if request.method == 'POST':
        try:
            apprecier.delete()
            return redirect('list_apprecies')  # Redirige vers la liste après suppression
        except Exception as e:
            return render(request, 'apprecies/delete.html', {'error': f"Erreur lors de la suppression : {str(e)}", 'apprecier': apprecier})

    return render(request, 'apprecies/delete.html', {'apprecier': apprecier})  # Confirmation de suppression






# --- LienSociale CRUD Operations ---
def list_LienSociale(request):
    if request.method == 'GET':
        Liens = LienSociale.objects.all()
        return render(request, 'session-admin/list.html', {'Liens': Liens})


def create_LienSociale(request):
    if request.method == 'POST':
        try:
            id_sout = request.POST.get('id_sout')
            id_prof = request.POST.get('id_prof')
            appreciation = request.POST.get('appreciation')

            Apprecier.objects.create(
                id_sout_id=id_sout,
                id_prof_id=id_prof,
                appreciation=appreciation
            )
            return redirect('list_apprecies')  # Redirige vers la liste après la création
        except Exception as e:
            return render(request, 'session-admin/form_gestion.html', {'error': f"Erreur lors de la création : {str(e)}"})

    Professeurs = Professeur.objects.all()
    return render(request, 'session-admin/form_gestion.html', {'view_name': 'create_LienSociale', 'Professeurs': Professeurs})  # Page de formulaire pour créer


def update_LienSociale(request, id):
    apprecier = get_object_or_404(Apprecier, id=id)
    if request.method == 'POST':
        try:
            apprecier.appreciation = request.POST.get('appreciation', apprecier.appreciation)
            apprecier.save()
            return redirect('list_apprecies')  # Redirige vers la liste après la mise à jour
        except Exception as e:
            return render(request, 'apprecies/update.html', {'error': f"Erreur lors de la mise à jour : {str(e)}", 'apprecier': apprecier})

    return render(request, 'apprecies/update.html', {'apprecier': apprecier})  # Page de formulaire pour modifier


def delete_LienSociale(request, id):
    apprecier = get_object_or_404(Apprecier, id=id)
    if request.method == 'POST':
        try:
            apprecier.delete()
            return redirect('list_apprecies')  # Redirige vers la liste après suppression
        except Exception as e:
            return render(request, 'apprecies/delete.html', {'error': f"Erreur lors de la suppression : {str(e)}", 'apprecier': apprecier})

    return render(request, 'apprecies/delete.html', {'apprecier': apprecier})  # Confirmation de suppression



# --- Professeurs CRUD Operations ---
def list_Professeurs(request):
    if request.method == 'GET':
        Professeurs = Professeur.objects.all()
        return render(request, 'session-admin/list.html', {'Professeurs': Professeurs})

def create_Professeurs(request): 

    return render(request, 'session-admin/form_gestion.html', {'view_name': 'create_Professeurs'})  # Page de formulaire pour créer




# --- Etudiants CRUD Operations ---
def list_Etudiants(request):
    if request.method == 'GET':
        Etudiants = Etudiant.objects.all()
        return render(request, 'session-admin/list.html', {'Etudiants': Etudiants})

def create_Etudiants(request): 

    Filieres = Filiere.objects.all()
    return render(request, 'session-admin/form_gestion.html', {'view_name': 'create_Etudiants', 'Filieres': Filieres})  # Page de formulaire pour créer





# --- Filieres CRUD Operations ---
def list_Filieres(request):
    if request.method == 'GET':
        Filieres = Filiere.objects.all()
        return render(request, 'session-admin/list.html', {'Filieres': Filieres})

def create_Filieres(request): 

    return render(request, 'session-admin/form_gestion.html', {'view_name': 'create_Filieres'})  # Page de formulaire pour créer




# --- Soutenances CRUD Operations ---
def list_Soutenances(request):
    if request.method == 'GET':
        Soutenances = Soutenance.objects.all()
        return render(request, 'session-admin/list.html', {'Soutenances': Soutenances})

def create_Soutenances(request): 

    Etudiants = Etudiant.objects.all()
    return render(request, 'session-admin/form_gestion.html', {'view_name': 'create_Soutenances', 'Etudiants': Etudiants})  # Page de formulaire pour créer




# --- Photos CRUD Operations ---
def list_Photos(request):
    if request.method == 'GET':
        Photos = Photo.objects.all()
        return render(request, 'session-admin/list.html', {'Photos': Photos})

def create_Photos(request): 

    return render(request, 'session-admin/form_gestion.html', {'view_name': 'create_Photos'})  # Page de formulaire pour créer




# --- Rapports CRUD Operations ---
def list_Rapports(request):
    if request.method == 'GET':
        Rapports = Rapport.objects.all()
        return render(request, 'session-admin/list.html', {'Rapports': Rapports})

def create_Rapports(request): 

    Soutenances = Soutenance.objects.all()
    return render(request, 'session-admin/form_gestion.html', {'view_name': 'create_Rapports', 'Soutenances': Soutenances})  # Page de formulaire pour créer




# --- Soutenances images CRUD Operations ---
def list_Soutenances_images(request):
    if request.method == 'GET':
        SoutenanceImages = SoutenanceImage.objects.all()
        return render(request, 'session-admin/list.html', {'SoutenanceImages': SoutenanceImages})

def create_Soutenancesimages(request): 

    Soutenances = Soutenance.objects.all()
    Photos = Photo.objects.all()
    return render(request, 'session-admin/form_gestion.html', {'view_name': 'create_Soutenancesimages', 'Soutenances': Soutenances, 'Photos': Photos})  # Page de formulaire pour créer

