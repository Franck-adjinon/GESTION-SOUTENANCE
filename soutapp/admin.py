from django.contrib import admin

from .models import Photo, Professeur, LienSociale, Message, Filiere, Etudiant, Soutenance, Rapport, Superviser, Apprecier, SoutenanceImage, Utilisateur, administrateur


@admin.register(Professeur)
class ProfesseurAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'spec', 'img', 'adr', 'tel', 'eml', 'create_date')  # Affiche ces colonnes dans la liste
    search_fields = ('nom_prof','prenom_prof',)             # Permet de rechercher par titre
    list_filter = ["created_at"]                 # ajout de filtrage à l’aide de l’attribut list_filter
    
    @admin.display(
        ordering="nom_prof",
        description="Nom - Prenom",
    )
    def full_name(self, obj):
        return obj.nom_prof + " " + obj.prenom_prof
    
    @admin.display(
        ordering="specialite_prof",
        description="Spécialité",
    )
    def spec(self, obj):
        return obj.specialite_prof
    
    @admin.display(
        ordering="image_prof",
        description="Photo professeur",
    )
    def img(self, obj):
        return obj.image_prof
    
    @admin.display(
        ordering="adresse_prof",
        description="Adresse professeur",
    )
    def adr(self, obj):
        return obj.adresse_prof
    
    @admin.display(
        ordering="telephone_prof",
        description="Contact professeur",
    )
    def tel(self, obj):
        return obj.telephone_prof
    
    @admin.display(
        ordering="email_prof",
        description="Email professeur",
    )
    def eml(self, obj):
        return obj.email_prof
    
    @admin.display(
        ordering="created_at",
        description="Date Ajout",
    )
    def create_date(self, obj):
        return obj.created_at


@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'eml', 'img', 'tel', 'id_filiere', 'create_date')  # Affiche ces colonnes dans la liste
    search_fields = ('nom_etu','prenom_etu',)             # Permet de rechercher par nom et prénom
    list_filter = ["created_at"]                 # ajout de filtrage à l’aide de l’attribut list_filter
    
    @admin.display(
        ordering="nom_etu",
        description="Nom - Prenom",
    )
    def full_name(self, obj):
        return obj.nom_etu + " " + obj.prenom_etu
    
    @admin.display(
        ordering="email_etu",
        description="Email etudiant",
    )
    def eml(self, obj):
        return obj.email_etu
    
    @admin.display(
        ordering="image_etu",
        description="Photo etudiant",
    )
    def img(self, obj):
        return obj.image_etu
    
    @admin.display(
        ordering="telephone_etu",
        description="Contact etudiant",
    )
    def tel(self, obj):
        return obj.telephone_etu
    
    @admin.display(
        ordering="created_at",
        description="Date Ajout",
    )
    def create_date(self, obj):
        return obj.created_at


@admin.register(Rapport)
class RapportAdmin(admin.ModelAdmin):
    list_display = ('id_sout', 'titre', 'create_date')  # Affiche ces colonnes dans la liste
    search_fields = ('id_sout','titre')             # Permet de rechercher par titre etsoutenance
    list_filter = ["id_sout", "created_at"]                 # ajout de filtrage à l’aide de l’attribut list_filter
    
    @admin.display(
        ordering="created_at",
        description="Date Ajout",
    )
    def create_date(self, obj):
        return obj.created_at


@admin.register(LienSociale)
class LienSocialeAdmin(admin.ModelAdmin):
    list_display = ('designation', 'lien', 'create_date', 'id_prof')  # Affiche ces colonnes dans la liste
    search_fields = ('designation',)             # Permet de rechercher par titre
    list_filter = ["id_prof"]                 # ajout de filtrage à l’aide de l’attribut list_filter
    
    @admin.display(
        ordering="created_at",
        description="Date Ajout",
    )
    def create_date(self, obj):
        return obj.created_at


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('titre', 'image', 'description', 'create_date')  # Affiche ces colonnes dans la liste
    search_fields = ('titre',)             # Permet de rechercher par titre
    list_filter = ["created_at"]                 # ajout de filtrage à l’aide de l’attribut list_filter
    
    @admin.display(
        ordering="created_at",
        description="Date Ajout",
    )
    def create_date(self, obj):
        return obj.created_at


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('status', 'sujet', 'eml', 'message', 'create_date')  # Affiche ces colonnes dans la liste
    search_fields = ('email_user',)             # Permet de rechercher par email
    list_filter = ["created_at", "status"]                 # ajout de filtrage à l’aide de l’attribut list_filter
    
    @admin.display(
        ordering="email_user",
        description="Email",
    )
    def eml(self, obj):
        return obj.email_user
    
    @admin.display(
        ordering="created_at",
        description="Date Ajout",
    )
    def create_date(self, obj):
        return obj.created_at


@admin.register(Filiere)
class FiliereAdmin(admin.ModelAdmin):
    list_display = ('designation', 'create_date')  # Affiche ces colonnes dans la liste
    search_fields = ('designation',)             # Permet de rechercher par titre
    list_filter = ["created_at"]                 # ajout de filtrage à l’aide de l’attribut list_filter
    
    @admin.display(
        ordering="created_at",
        description="Date Ajout",
    )
    def create_date(self, obj):
        return obj.created_at


@admin.register(Soutenance)
class SoutenanceAdmin(admin.ModelAdmin):
    list_display = ('theme', 'HD', 'HF', 'dts', 'lieu', 'is_finish', 'create_date', 'id_etudiant')  # Affiche ces colonnes dans la liste
    search_fields = ('theme',)             # Permet de rechercher par titre
    list_filter = ["created_at", "is_finish"]                 # ajout de filtrage à l’aide de l’attribut list_filter
    
    @admin.display(
        ordering="Heure_deb",
        description="Heure début",
    )
    def HD(self, obj):
        return obj.Heure_deb
    
    @admin.display(
        ordering="Heure_fin",
        description="Heure Fin",
    )
    def HF(self, obj):
        return obj.Heure_fin
    
    @admin.display(
        ordering="Date_sout",
        description="Date Soutenance",
    )
    def dts(self, obj):
        return obj.Date_sout
    
    @admin.display(
        ordering="created_at",
        description="Date Ajout",
    )
    def create_date(self, obj):
        return obj.created_at


@admin.register(Superviser)
class SuperviserAdmin(admin.ModelAdmin):
    list_display = ('id_sout', 'id_prof', 'role', 'create_date')  # Affiche ces colonnes dans la liste
    search_fields = ('id_sout',)             # Permet de rechercher par soutenance
    list_filter = ["id_sout"]                 # ajout de filtrage à l’aide de l’attribut list_filter
    
    @admin.display(
        ordering="create_at",
        description="Date Ajout",
    )
    def create_date(self, obj):
        return obj.create_at


@admin.register(Apprecier)
class ApprecierAdmin(admin.ModelAdmin):
    list_display = ('id_sout', 'id_prof', 'appreciation', 'create_date')  # Affiche ces colonnes dans la liste
    list_filter = ["id_sout"]                 # ajout de filtrage à l’aide de l’attribut list_filter
    
    @admin.display(
        ordering="create_at",
        description="Date Ajout",
    )
    def create_date(self, obj):
        return obj.create_at


@admin.register(SoutenanceImage)
class SoutenanceImageAdmin(admin.ModelAdmin):
    list_display = ('id_sout', 'id_photo', 'pour', 'create_date')  # Affiche ces colonnes dans la liste
    list_filter = ["id_sout"]                 # ajout de filtrage à l’aide de l’attribut list_filter
    
    @admin.display(
        ordering="created_at",
        description="Date Ajout",
    )
    def create_date(self, obj):
        return obj.created_at


@admin.register(administrateur)
class administrateurAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'eml', 'create_date')  # Affiche ces colonnes dans la liste
    search_fields = ('nom_admin','prenom_admin',)             # Permet de rechercher par titre
    list_filter = ["created_at"]                 # ajout de filtrage à l’aide de l’attribut list_filter
    
    @admin.display(
        ordering="nom_admin",
        description="Nom - Prenom",
    )
    def full_name(self, obj):
        return obj.nom_admin + " " + obj.prenom_admin
    
    
    @admin.display(
        ordering="email",
        description="Email admin",
    )
    def eml(self, obj):
        return obj.email
    
    @admin.display(
        ordering="created_at",
        description="Date Ajout",
    )
    def create_date(self, obj):
        return obj.created_at


@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'eml', 'create_date')  # Affiche ces colonnes dans la liste
    search_fields = ('nom_user','prenom_user',)             # Permet de rechercher par titre
    list_filter = ["created_at"]                 # ajout de filtrage à l’aide de l’attribut list_filter
    
    @admin.display(
        ordering="nom_user",
        description="Nom - Prenom",
    )
    def full_name(self, obj):
        return obj.nom_user + " " + obj.prenom_user
    
    
    @admin.display(
        ordering="email",
        description="Email admin",
    )
    def eml(self, obj):
        return obj.email
    
    @admin.display(
        ordering="created_at",
        description="Date Ajout",
    )
    def create_date(self, obj):
        return obj.created_at