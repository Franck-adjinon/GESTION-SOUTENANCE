from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('connexion', views.connexion, name='connexion'),
    path('Tableau de Bord', views.dashbord, name='dashbord'),
    path('blog', views.blog, name='blog'),
    path('article_detail', views.article_detail, name='article_detail'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('prof', views.prof, name='prof'),
    path('prof_detail', views.prof_detail, name='prof_detail'),
    path('user_profil', views.user_profil, name='user_profil'),
    
    
    
    
    
    
    
] 