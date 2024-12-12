from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'session-templates/pages/create-account.html')

def connexion(request):
    return render(request, 'session-templates/pages/login.html')

def dashbord(request):
    return render(request, 'session-templates/index.html')

def blog(request):
    return render(request, 'session-blog/blog.html')

def article_detail(request):
    return render(request, 'session-blog/single.html')

#user_profil
def contact(request):
    return render(request, 'session-blog/contact.html')

def faq(request):
    return render(request, 'session-blog/faq.html')

def prof(request):
    return render(request, 'session-blog/prof.html')

def prof_detail(request):
    return render(request, 'session-blog/prof_detail.html')

def user_profil(request):
    return render(request, 'session-blog/user_profil.html')