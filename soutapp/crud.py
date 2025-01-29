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
        supervisers = Superviser.objects.all().order_by('-create_at')
        return render(request, 'session-admin/list.html', {'supervisers': supervisers})


def create_superviser(request):
    if request.method == 'POST':
        try:
            id_sout = request.POST.get('id_sout')
            id_prof = request.POST.get('id_prof')
            role = request.POST.get('role')
            
            # Récupération des objets correspondant
            sout = get_object_or_404(Soutenance, id_sout=id_sout)
            prof = get_object_or_404(Professeur, id_prof=id_prof)

            Superviser.objects.create(
                id_sout=sout,
                id_prof=prof,
                role=role
            )
            return redirect('list_supervisers')  # Redirige vers la liste après la création
        except Exception as e:
            return render(request, 'session-admin/form_gestion.html', {'error': f"Erreur lors de la création : {str(e)}"})

    Soutenances = Soutenance.objects.all().order_by('-created_at')
    Professeurs = Professeur.objects.all().order_by('-created_at')
    return render(request, 'session-admin/form_gestion.html', {'view_name': 'create_superviser', 'Professeurs': Professeurs, 'Soutenances': Soutenances})  # Page de formulaire pour créer


def update_superviser(request, id):
    superviser = get_object_or_404(Superviser, id=id)
    if request.method == 'POST':
        try: 
            superviser.role = request.POST.get('role', superviser.role)
            superviser.save()
            return redirect('list_supervisers')  # Redirige vers la liste après la mise à jour
        except Exception as e:
            return render(request, 'session-admin/form_update.html', {'error': f"Erreur lors de la mise à jour : {str(e)}", 'superviser': superviser})

    return render(request, 'session-admin/form_update.html', {'view_name': 'update_superviser', 'superviseur': superviser})  # Page de formulaire pour modifier


def delete_superviser(request, id):
    try: 
        
        # Récupérer l'objet Superviser 
        sup = get_object_or_404(Superviser, id=id)
        
        sup.delete() 
        return redirect('list_supervisers') 

    except Exception as e:
        return render(request, 'session-admin/list.html', {
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

            # Récupération des objets correspondant
            sout = get_object_or_404(Soutenance, id_sout=id_sout)
            prof = get_object_or_404(Professeur, id_prof=id_prof)
            
            Apprecier.objects.create(
                id_sout=sout,
                id_prof=prof,
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
            return render(request, 'session-admin/form_update.html', {'error': f"Erreur lors de la mise à jour : {str(e)}", 'apprecier': apprecier})

    return render(request, 'session-admin/form_update.html', {'view_name': 'update_apprecier', 'apprecier': apprecier})  # Page de formulaire pour modifier


def delete_apprecier(request, id):
    apprecier = get_object_or_404(Apprecier, id=id) 
    try:
        apprecier.delete()
        return redirect('list_apprecies')  # Redirige vers la liste après suppression
    except Exception as e:
        return render(request, 'session-admin/list.html', {'error': f"Erreur lors de la suppression : {str(e)}"})





# --- LienSociale CRUD Operations ---
def list_LienSociale(request):
    if request.method == 'GET':
        Liens = LienSociale.objects.all()
        return render(request, 'session-admin/list.html', {'Liens': Liens})


def create_LienSociale(request):
    if request.method == 'POST':
        try:
            designation = request.POST.get('designation')
            lien = request.POST.get('lien')
            id_prof = request.POST.get('id_prof')
            
            # Récupération des objets correspondant 
            prof = get_object_or_404(Professeur, id_prof=id_prof)

            LienSociale.objects.create( 
                designation=designation,
                lien=lien,
                id_prof=prof,
            )
            return redirect('list_LienSociale')  # Redirige vers la liste après la création
        except Exception as e:
            return render(request, 'session-admin/form_gestion.html', {'error': f"Erreur lors de la création : {str(e)}"})

    Professeurs = Professeur.objects.all()
    return render(request, 'session-admin/form_gestion.html', {'view_name': 'create_LienSociale', 'Professeurs': Professeurs})  # Page de formulaire pour créer


def update_LienSociale(request, id):
    lien = get_object_or_404(LienSociale, id_lien=id)
    if request.method == 'POST':
        try:
            
            back_up = get_object_or_404(LienSociale, id_lien=id)
            
            lien.designation = request.POST.get('designation', lien.designation)
            lien.lien = request.POST.get('lien', lien.lien)
            
            # contrôle des champs vides 
            if lien.designation == '':
                lien.designation = back_up.designation
            if lien.lien == '':
                lien.lien = back_up.lien
            
            
            lien.save()
            return redirect('list_LienSociale')  # Redirige vers la liste après la mise à jour
        except Exception as e:
            return render(request, 'session-admin/form_update.html', {'error': f"Erreur lors de la mise à jour : {str(e)}", 'lien': lien})

    return render(request, 'session-admin/form_update.html', {'view_name': 'update_LienSociale', 'lien': lien})  # Page de formulaire pour modifier


def delete_LienSociale(request, id):
    try:
        
        lien = get_object_or_404(LienSociale, id_lien=id)
        lien.delete()
        return redirect('list_LienSociale')  # Redirige vers la liste après suppression
    
    except Exception as e: 
        return render( request, 'session-admin/list.html', {
            'error': f"Erreur lors de la suppression : {str(e)}"
        })



# --- Professeurs CRUD Operations ---
def list_Professeurs(request):
    if request.method == 'GET':
        Professeurs = Professeur.objects.all()
        return render(request, 'session-admin/list.html', {'Professeurs': Professeurs})

def create_Professeurs(request): 
    if request.method == 'POST':
        try:
            nom_prof = request.POST.get('nom_prof')
            prenom_prof = request.POST.get('prenom_prof')
            specialite_prof = request.POST.get('specialite_prof')
            image_prof = request.FILES.get('image_prof')
            adresse_prof = request.POST.get('adresse_prof')
            telephone_prof = request.POST.get('telephone_prof')
            email_prof = request.POST.get('email_prof')

            # Validation des champs (par exemple, vérifier qu'ils ne sont pas vides)
            if not (nom_prof and prenom_prof and email_prof):
                raise ValueError("Les champs Nom, Prénom et Email sont obligatoires.")
            
            Professeur.objects.create(
                nom_prof=nom_prof,
                prenom_prof=prenom_prof,
                specialite_prof=specialite_prof,
                image_prof=image_prof,
                adresse_prof=adresse_prof,
                telephone_prof=telephone_prof,
                email_prof=email_prof
            )
            return redirect('list_Professeurs')  # Redirige vers la liste après la création
        except Exception as e:
            return render(request, 'session-admin/form_gestion.html', {'error': f"Erreur lors de la création : {str(e)}"})
    
    
    return render(request, 'session-admin/form_gestion.html', {'view_name': 'create_Professeurs'})  # Page de formulaire pour créer

def update_professeurs(request, id):
    prof = get_object_or_404(Professeur, id_prof=id)
    if request.method == 'POST':
        try:
            
            back_up = get_object_or_404(Professeur, id_prof=id)
            
            prof.nom_prof = request.POST.get('nom_prof', prof.nom_prof)
            prof.prenom_prof = request.POST.get('prenom_prof', prof.prenom_prof)
            prof.specialite_prof = request.POST.get('specialite_prof', prof.specialite_prof)
            prof.image_prof = request.FILES.get('image_prof', prof.image_prof)
            prof.adresse_prof = request.POST.get('adresse_prof', prof.adresse_prof)
            prof.telephone_prof = request.POST.get('telephone_prof', prof.telephone_prof)
            prof.email_prof = request.POST.get('email_prof', prof.email_prof)
            
            # contrôle des champs vides 
            if prof.nom_prof == '':
                prof.nom_prof = back_up.nom_prof
            if not prof.image_prof :
                prof.image_prof = back_up.image_prof
            if prof.prenom_prof == '':
                prof.prenom_prof = back_up.prenom_prof
            if prof.specialite_prof == '':
                prof.specialite_prof = back_up.specialite_prof
            if prof.adresse_prof == '':
                prof.adresse_prof = back_up.adresse_prof
            if prof.telephone_prof == '':
                prof.telephone_prof = back_up.telephone_prof
            if prof.email_prof == '':
                prof.email_prof = back_up.email_prof
            
            
            prof.save()
            return redirect('list_Professeurs')  # Redirige vers la liste après la mise à jour
        except Exception as e:
            return render(request, 'session-admin/form_update.html', {'error': f"Erreur lors de la mise à jour : {str(e)}", 'prof': prof})

    return render(request, 'session-admin/form_update.html', {'view_name': 'update_professeurs', 'prof': prof})  # Page de formulaire pour modifier

def delete_professeurs(request, id):
    try:
        prof = get_object_or_404(Professeur, id_prof=id)
        prof.delete()
        return redirect('list_Professeurs')
    except Exception as e:
        return render( request, 'session-admin/list.html', {
            'error': f"Erreur lors de la suppression : {str(e)}"
        })


# --- Etudiants CRUD Operations ---
def list_Etudiants(request):
    if request.method == 'GET':
        Etudiants = Etudiant.objects.all()
        return render(request, 'session-admin/list.html', {'Etudiants': Etudiants})

def create_Etudiants(request): 
    if request.method == 'POST':
        try:
            nom_etu = request.POST.get('nom_etu')
            prenom_etu = request.POST.get('prenom_etu')
            email_etu = request.POST.get('email_etu')
            image_etu = request.FILES.get('image_etu')
            telephone_etu = request.POST.get('telephone_etu')
            id_filiere = request.POST.get('id_filiere')
            

            # Validation des champs (par exemple, vérifier qu'ils ne sont pas vides)
            if not (nom_etu and prenom_etu and email_etu):
                raise ValueError("Les champs Nom, Prénom et Email sont obligatoires.")
            
            # Récupération de l'objet Filiere correspondant
            filiere = get_object_or_404(Filiere, id_filiere=id_filiere)
            
            Etudiant.objects.create(
                nom_etu=nom_etu,
                prenom_etu=prenom_etu,
                email_etu=email_etu,
                image_etu=image_etu,
                telephone_etu=telephone_etu,
                id_filiere = filiere,
            )
            return redirect('list_Etudiants')  # Redirige vers la liste après la création
        except Exception as e:
            return render(request, 'session-admin/form_gestion.html', {'error': f"Erreur lors de la création : {str(e)}"})

    Filieres = Filiere.objects.all()
    return render(request, 'session-admin/form_gestion.html', {'view_name': 'create_Etudiants', 'Filieres': Filieres})  # Page de formulaire pour créer

def update_etudiant(request, id):
    Etu = get_object_or_404(Etudiant, id_etudiant=id)
    if request.method == 'POST':
        try:
            
            back_up = get_object_or_404(Etudiant, id_etudiant=id)
            
            Etu.nom_etu = request.POST.get('nom_etu', Etu.nom_etu)
            Etu.prenom_etu = request.POST.get('prenom_etu', Etu.prenom_etu)
            Etu.email_etu = request.POST.get('email_etu', Etu.email_etu)
            Etu.image_etu = request.FILES.get('image_etu', Etu.image_etu)
            Etu.telephone_etu = request.POST.get('telephone_etu', Etu.telephone_etu)
            id_filiere = request.POST.get('id_filiere')
            
            # Récupération de l'objet Filiere correspondant
            filiere = get_object_or_404(Filiere, id_filiere=id_filiere)
            
            Etu.id_filiere = filiere
            
            # contrôle des champs vides 
            if Etu.nom_etu == '':
                Etu.nom_etu = back_up.nom_etu
            if not Etu.image_etu :
                Etu.image_etu = back_up.image_etu
            if Etu.prenom_etu == '':
                Etu.prenom_etu = back_up.prenom_etu
            if Etu.email_etu == '':
                Etu.email_etu = back_up.email_etu
            if Etu.telephone_etu == '':
                Etu.telephone_etu = back_up.telephone_etu
            if Etu.id_filiere == '':
                Etu.id_filiere = back_up.id_filiere 
            
            
            Etu.save()
            return redirect('list_Etudiants')  # Redirige vers la liste après la mise à jour
        except Exception as e:
            return render(request, 'session-admin/form_update.html', {'error': f"Erreur lors de la mise à jour : {str(e)}", 'Etu': Etu})

    filieres = Filiere.objects.all()
    return render(request, 'session-admin/form_update.html', {'view_name': 'update_etudiant', 'Etu': Etu, 'filieres': filieres})  # Page de formulaire pour modifier

def delete_etudiant(request, id):
    try:
        etu = get_object_or_404(Etudiant, id_etudiant=id)
        etu.delete()
        return redirect('list_Etudiants')
    except Exception as e:
        return render( request, 'session-admin/list.html', {
            'error': f"Erreur lors de la suppression : {str(e)}"
        })



# --- Filieres CRUD Operations ---
def list_Filieres(request):
    if request.method == 'GET':
        Filieres = Filiere.objects.all()
        return render(request, 'session-admin/list.html', {'Filieres': Filieres})

def create_Filieres(request): 
    if request.method == 'POST':
        try:
            designation = request.POST.get('designation') 

            Filiere.objects.create(
                designation=designation, 
            )
            return redirect('list_Filieres')  # Redirige vers la liste après la création
        except Exception as e:
            return render(request, 'session-admin/form_gestion.html', {'error': f"Erreur lors de la création : {str(e)}"})


    return render(request, 'session-admin/form_gestion.html', {'view_name': 'create_Filieres'})  # Page de formulaire pour créer

def update_filiere(request, id):
    fil = get_object_or_404(Filiere, id_filiere=id)
    if request.method == 'POST':
        try:
            
            back_up = get_object_or_404(Filiere, id_filiere=id)
            
            fil.designation = request.POST.get('designation', fil.designation)
            
            # contrôle des champs vides 
            if fil.designation == '':
                fil.designation = back_up.designation 
            
            
            fil.save()
            return redirect('list_Filieres')  # Redirige vers la liste après la mise à jour
        except Exception as e:
            return render(request, 'session-admin/form_update.html', {'error': f"Erreur lors de la mise à jour : {str(e)}", 'fil': fil})

    return render(request, 'session-admin/form_update.html', {'view_name': 'update_filiere', 'fil': fil})  # Page de formulaire pour modifier

def delete_filiere(request, id):
    try:
        fil = get_object_or_404(Filiere, id_filiere=id)
        fil.delete()
        return redirect('list_Filieres')
    except Exception as e:
        return render( request, 'session-admin/list.html', {
            'error': f"Erreur lors de la suppression : {str(e)}"
        })


# --- Soutenances CRUD Operations ---
def list_Soutenances(request):
    if request.method == 'GET':
        Soutenances = Soutenance.objects.all()
        return render(request, 'session-admin/list.html', {'Soutenances': Soutenances})

def create_Soutenances(request): 
    if request.method == 'POST':
        try:
            theme = request.POST.get('theme')
            Heure_deb = request.POST.get('Heure_deb')
            Heure_fin = request.POST.get('Heure_fin')
            Date_sout = request.POST.get('Date_sout')
            lieu = request.POST.get('lieu')
            is_finish = request.POST.get('is_finish') == "on"
            id_etudiant = request.POST.get('id_etudiant') 

            # Récupération des objets correspondant
            etu = get_object_or_404(Etudiant, id_etudiant=id_etudiant) 
            
            Soutenance.objects.create(
                theme = theme,
                Heure_deb = Heure_deb,
                Heure_fin = Heure_fin,
                Date_sout = Date_sout,
                lieu = lieu,
                is_finish = is_finish,
                id_etudiant=etu,
            ) 
            return redirect('list_Soutenances')  # Redirige vers la liste après la création
        except Exception as e:
            return render(request, 'session-admin/form_gestion.html', {'error': f"Erreur lors de la création : {str(e)}", 'view_name': 'create_apprecier'})


    Etudiants = Etudiant.objects.all()
    return render(request, 'session-admin/form_gestion.html', {'view_name': 'create_Soutenances', 'Etudiants': Etudiants})  # Page de formulaire pour créer

def update_soutenance(request, id):
    sout = get_object_or_404(Soutenance, id_sout=id)
    if request.method == 'POST':
        try:
            
            back_up = get_object_or_404(Soutenance, id_sout=id)
            
            sout.theme = request.POST.get('theme', sout.theme)
            sout.Heure_deb = request.POST.get('Heure_deb', sout.Heure_deb)
            sout.Heure_fin = request.POST.get('Heure_fin', sout.Heure_fin)
            sout.Date_sout = request.POST.get('Date_sout', sout.Date_sout)
            sout.lieu = request.POST.get('lieu', sout.lieu)
            sout.is_finish = 'is_finish' in request.POST
            id_etudiant = request.POST.get('id_etudiant')
            
            # Récupération de l'objet Filiere correspondant
            etu = get_object_or_404(Etudiant, id_etudiant=id_etudiant)
            
            sout.id_etudiant = etu
            
            # contrôle des champs vides 
            if sout.theme == '':
                sout.theme = back_up.theme 
            if sout.Heure_deb == '':
                sout.Heure_deb = back_up.Heure_deb 
            if sout.Heure_fin == '':
                sout.Heure_fin = back_up.Heure_fin 
            if sout.Date_sout == '':
                sout.Date_sout = back_up.Date_sout 
            if sout.lieu == '':
                sout.lieu = back_up.lieu 
            if sout.is_finish == '':
                sout.is_finish = back_up.is_finish 
            if sout.id_etudiant == '':
                sout.id_etudiant = back_up.id_etudiant 
            
            
            sout.save()
            return redirect('list_Soutenances')  # Redirige vers la liste après la mise à jour
        except Exception as e:
            return render(request, 'session-admin/form_update.html', {'error': f"Erreur lors de la mise à jour : {str(e)}", 'sout': sout})

    etudiant = Etudiant.objects.all()
    return render(request, 'session-admin/form_update.html', {'view_name': 'update_soutenance', 'sout': sout, 'etudiant': etudiant})  # Page de formulaire pour modifier

def delete_soutenances(request, id):
    try:
        sout = get_object_or_404(Soutenance, id_sout=id)
        sout.delete()
        return redirect('list_Soutenances')
    except Exception as e:
        return render( request, 'session-admin/list.html', {
            'error': f"Erreur lors de la suppression : {str(e)}"
        })


# --- Photos CRUD Operations ---
def list_Photos(request):
    if request.method == 'GET':
        Photos = Photo.objects.all()
        return render(request, 'session-admin/list.html', {'Photos': Photos})

def create_Photos(request): 
    if request.method == 'POST':
        try:
            titre = request.POST.get('titre')
            image = request.FILES.get('image')
            description = request.POST.get('description') 
            
            Photo.objects.create(
                titre = titre,
                image = image,
                description = description, 
            ) 
            return redirect('list_Photos')  # Redirige vers la liste après la création
        except Exception as e:
            return render(request, 'session-admin/form_gestion.html', {'error': f"Erreur lors de la création : {str(e)}", 'view_name': 'create_apprecier'})


    return render(request, 'session-admin/form_gestion.html', {'view_name': 'create_Photos'})  # Page de formulaire pour créer

def update_photo(request, id):
    pht = get_object_or_404(Photo, id_photo=id)
    if request.method == 'POST':
        try:
            
            back_up = get_object_or_404(Photo, id_photo=id)
            
            pht.titre = request.POST.get('titre', pht.titre)
            pht.image = request.FILES.get('image', pht.image)
            pht.description = request.POST.get('description', pht.description)
            
            # contrôle des champs vides 
            if pht.titre == '':
                pht.titre = back_up.titre
            if not pht.image :
                pht.image = back_up.image
            if not pht.description :
                pht.description = back_up.description
            
            
            pht.save()
            return redirect('list_Photos')  # Redirige vers la liste après la mise à jour
        except Exception as e:
            return render(request, 'session-admin/form_update.html', {'error': f"Erreur lors de la mise à jour : {str(e)}", 'pht': pht})

    return render(request, 'session-admin/form_update.html', {'view_name': 'update_photo', 'pht': pht})  # Page de formulaire pour modifier

def delete_photo(request, id):
    try:
        pt = get_object_or_404(Photo, id_photo=id)
        pt.delete()
        return redirect('list_Photos')
    except Exception as e :
        return render( request, 'session-admin/list.html', {
            'error': f"Erreur lors de la suppression : {str(e)}"
        })



# --- Rapports CRUD Operations ---
def list_Rapports(request):
    if request.method == 'GET':
        Rapports = Rapport.objects.all()
        return render(request, 'session-admin/list.html', {'Rapports': Rapports})

def create_Rapports(request):
    if request.method == 'POST':
        try:
            titre = request.POST.get('titre')
            sommaire = request.POST.get('sommaire')
            contenu = request.POST.get('contenu')
            id_sout = request.POST.get('id_sout') 

            # Récupération des objets correspondant
            sout = get_object_or_404(Soutenance, id_sout=id_sout) 
            
            Rapport.objects.create(
                titre=titre,
                sommaire=sommaire,
                contenu=contenu,
                id_sout=sout,
            ) 
            return redirect('list_Rapports')  # Redirige vers la liste après la création
        except Exception as e:
            return render(request, 'session-admin/form_gestion.html', {'error': f"Erreur lors de la création : {str(e)}", 'view_name': 'create_apprecier'})


    Soutenances = Soutenance.objects.all()
    return render(request, 'session-admin/form_gestion.html', {'view_name': 'create_Rapports', 'Soutenances': Soutenances})  # Page de formulaire pour créer

def update_rapports(request, id):
    rap = get_object_or_404(Rapport, id_rapport=id)
    if request.method == 'POST':
        try:
            
            back_up = get_object_or_404(Rapport, id_rapport=id)
            
            rap.titre = request.POST.get('titre', rap.titre)
            rap.sommaire = request.POST.get('sommaire', rap.sommaire)
            rap.contenu = request.POST.get('contenu', rap.contenu)
            id_sout = request.POST.get('id_sout')
            
            # Récupération de l'objet Soutenance correspondant
            sout = get_object_or_404(Soutenance, id_sout=id_sout)
            
            rap.id_sout = sout
            
            # contrôle des champs vides 
            if rap.titre == '':
                rap.titre = back_up.titre 
            if rap.sommaire == '':
                rap.sommaire = back_up.sommaire 
            if rap.contenu == '':
                rap.contenu = back_up.contenu 
            if rap.id_sout == '':
                rap.id_sout = back_up.id_sout 
            
            
            rap.save()
            return redirect('list_Rapports')  # Redirige vers la liste après la mise à jour
        except Exception as e:
            return render(request, 'session-admin/form_update.html', {'error': f"Erreur lors de la mise à jour : {str(e)}", 'rap': rap})

    souts = Soutenance.objects.all()
    return render(request, 'session-admin/form_update.html', {'view_name': 'update_rapports', 'rap': rap, 'souts': souts})  # Page de formulaire pour modifier

def delete_rapports(request, id):
    try:
        rp = get_object_or_404(Rapport, id_rapport=id)
        rp.delete()
        return redirect('list_Rapports')
    except Exception as e:
        return render( request, 'session-admin/list.html', {
            'error': f"Erreur lors de la suppression : {str(e)}"
        })


# --- Soutenances images CRUD Operations ---
def list_Soutenances_images(request):
    if request.method == 'GET':
        SoutenanceImages = SoutenanceImage.objects.all()
        return render(request, 'session-admin/list.html', {'SoutenanceImages': SoutenanceImages})

def create_Soutenancesimages(request): 
    if request.method == 'POST':
        try:
            id_sout = request.POST.get('id_sout')
            id_photo = request.POST.get('id_photo')
            pour = request.POST.get('pour')

            # Récupération des objets correspondant
            sout = get_object_or_404(Soutenance, id_sout=id_sout)
            phot = get_object_or_404(Photo, id_photo=id_photo)
            
            SoutenanceImage.objects.create(
                id_sout=sout,
                id_photo=phot,
                pour=pour
            ) 
            return redirect('list_Soutenances_images')  # Redirige vers la liste après la création
        except Exception as e:
            return render(request, 'session-admin/form_gestion.html', {'error': f"Erreur lors de la création : {str(e)}", 'view_name': 'create_apprecier'})


    Soutenances = Soutenance.objects.all()
    Photos = Photo.objects.all()
    return render(request, 'session-admin/form_gestion.html', {'view_name': 'create_Soutenancesimages', 'Soutenances': Soutenances, 'Photos': Photos})  # Page de formulaire pour créer

def update_soutenanceImage(request, id):
    sout = get_object_or_404(SoutenanceImage, id=id)
    if request.method == 'POST':
        try: 
            sout.pour = request.POST.get('pour', sout.pour)
            sout.save()
            return redirect('list_Soutenances_images')  # Redirige vers la liste après la mise à jour
        except Exception as e:
            return render(request, 'session-admin/form_update.html', {'error': f"Erreur lors de la mise à jour : {str(e)}", 'sout': sout})

    pht = Photo.objects.all()
    return render(request, 'session-admin/form_update.html', {'view_name': 'update_soutenanceImage', 'sout': sout, 'pht': pht})  # Page de formulaire pour modifier

def delete_soutenanceImage(request, id):
    try:
        simg = get_object_or_404(SoutenanceImage, id=id)
        simg.delete()
        return redirect('list_Soutenances_images')
    except Exception as e:
        return render( request, 'session-admin/list.html', {
            'error': f"Erreur lors de la suppression : {str(e)}"
        })