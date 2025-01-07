from django.urls import path
from . import views

from .views import CustomLoginView
from .views import logout_view
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static


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

    # TODO: Affiche la section profil 
    path('user_profil', views.user_profil, name='user_profil'),

    # TODO: Affiche la page de connexion
    path('connexion/', CustomLoginView.as_view(), name='login'),

    # TODO: Affuche la page de déconnexion
    path('deconnexion/', logout_view, name='logout'),

    # TODO: Affiche les informations de l'utilisateur connecter
    path('user_profil/<int:pk>', views.UserDetail.as_view(), name='user_profil'),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)