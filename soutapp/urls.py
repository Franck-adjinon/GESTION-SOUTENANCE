from django.urls import path
from . import crud
from .views import CustomLoginView, login_admin
from .views import logout_view, logout_admin_view 
from django.conf import settings
from django.conf.urls.static import static
from . import views  

urlpatterns = [
    
    # TODO: Affiche la page d'inscription
    path('', views.index, name='index'), 
    
    # TODO: Affiche l'accueil
    path('Tableau de Bord', views.dashbord, name='dashbord'),
    
    # TODO: Affiche les soutenances à venir 
    path('blog_next', views.blog_next, name='blog_next'),

    # TODO: Affiches les soutenances terminer
    path('blog_past', views.blog_past, name='blog_past'),

    # TODO: Détails des soutenances à venir
    path('sout_detail/<int:pk>', views.SoutDetail.as_view(), name='sout_detail'),
    
    # TODO: Détails des soutenances terminer
    path('sout_detail_finish/<int:pk>', views.SoutDetailFinish.as_view(), name='sout_detail_finish'),

    # TODO: Section contact
    path('contact', views.contact, name='contact'),

    # TODO: Section faq 
    path('faq', views.faq, name='faq'),

    # TODO: Détails des professeurs 
    path('prof_detail/<int:pk>', views.ProfDetail.as_view(), name='prof_detail'),
    
    # TODO: Affiche les professeurs
    path('prof', views.prof, name='prof'),

    # TODO: Affiche la page de connexion
    path('connexion/', CustomLoginView.as_view(), name='login'),

    # TODO: Affuche la page de déconnexion
    path('deconnexion/', logout_view, name='logout'),
    
    # Afficher l'interface de connexion des administrateurs
    path('administrateur/', login_admin.as_view(), name='administrateur'),
    
    # Afficher dashboard des administrateurs
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
    
    # Déconnecter l'administrateur
    path('deconnexion-admin/', logout_admin_view, name='logout_admin'),
    

    #Début des urls vers les fonctions crud pour la gestion des autres tables
    # Superviser CRUD URLs
    path('admin-dashboard-supervisers/', crud.list_supervisers, name='list_supervisers'),
    path('admin-dashboard-supervisers/create/', crud.create_superviser, name='create_superviser'),
    path('admin-dashboard-supervisers/update/<int:id>/', crud.update_superviser, name='update_superviser'),
    path('admin-dashboard-supervisers/delete/<int:id_prof>/<int:id_sout>/<str:create_at>/', crud.delete_superviser, name='delete_superviser'),

    # Apprecier CRUD URLs
    path('admin-dashboard-apprecies/', crud.list_apprecies, name='list_apprecies'),
    path('admin-dashboard-apprecies/create/', crud.create_apprecier, name='create_apprecier'),
    path('admin-dashboard-apprecies/update/<int:id>/', crud.update_apprecier, name='update_apprecier'),
    path('admin-dashboard-apprecies/delete/<int:id>/', crud.delete_apprecier, name='delete_apprecier'),
    
    # LienSociale CRUD URLs
    path('admin-dashboard-LienSociale/', crud.list_LienSociale, name='list_LienSociale'),
    path('admin-dashboard-LienSociale/create/', crud.create_LienSociale, name='create_LienSociale'),
    path('admin-dashboard-LienSociale/update/<int:id>/', crud.update_LienSociale, name='update_LienSociale'),
    path('admin-dashboard-LienSociale/delete/<int:id>/', crud.delete_LienSociale, name='delete_LienSociale'),
    
    # Professeurs CRUD URLs
    path('admin-dashboard-Professeurs/', crud.list_Professeurs, name='list_Professeurs'),
    path('admin-dashboard-Professeurs/create/', crud.create_Professeurs, name='create_Professeurs'),
    
    # list_Etudiants CRUD URLs
    path('admin-dashboard-Etudiants/', crud.list_Etudiants, name='list_Etudiants'),
    path('admin-dashboard-Etudiants/create/', crud.create_Etudiants, name='create_Etudiants'),
    
    # Photos CRUD URLs
    path('admin-dashboard-Photos/', crud.list_Photos, name='list_Photos'),
    path('admin-dashboard-Photos/create/', crud.create_Photos, name='create_Photos'),
    
    # Filieres CRUD URLs 
    path('admin-dashboard-Filieres/', crud.list_Filieres, name='list_Filieres'),
    path('admin-dashboard-Filieres/create/', crud.create_Filieres, name='create_Filieres'),
    
    # Soutenances CRUD URLs 
    path('admin-dashboard-Soutenances/', crud.list_Soutenances, name='list_Soutenances'),
    path('admin-dashboard-Soutenances/create/', crud.create_Soutenances, name='create_Soutenances'),
    
    # Rapports CRUD URLs 
    path('admin-dashboard-Rapports/', crud.list_Rapports, name='list_Rapports'),
    path('admin-dashboard-Rapports/create/', crud.create_Rapports, name='create_Rapports'),
    
    # Soutenances_images CRUD URLs 
    path('admin-dashboard-Soutenancesimages/', crud.list_Soutenances_images, name='list_Soutenances_images'),
    path('admin-dashboard-Soutenancesimages/create/', crud.create_Soutenancesimages, name='create_Soutenancesimages'),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)