from rest_framework import viewsets
from .models import Chercheur, ProjetDeRecherche, Publication
from .serializers import ChercheurSerializer, ProjetDeRechercheSerializer, PublicationSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def liste_chercheurs(request):
    chercheurs = Chercheur.objects.all()
    return render(request, 'gestion/chercheur_list.html', {'chercheurs': chercheurs})

@login_required
def ajouter_chercheur(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        specialite = request.POST.get('specialite')
        Chercheur.objects.create(nom=nom, specialite=specialite)
        return redirect('liste_chercheurs')
    return render(request, 'gestion/chercheur_form.html')

@login_required
def liste_projets(request):
    projets = ProjetDeRecherche.objects.all()
    return render(request, 'gestion/projet_list.html', {'projets': projets})

@login_required
def ajouter_projet(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        date_debut = request.POST.get('date_debut')
        date_fin_prevue = request.POST.get('date_fin_prevue')
        chef_de_projet_id = request.POST.get('chef_de_projet')
        chef_de_projet = Chercheur.objects.get(id=chef_de_projet_id)
        ProjetDeRecherche.objects.create(
            titre=titre,
            description=description,
            date_debut=date_debut,
            date_fin_prevue=date_fin_prevue,
            chef_de_projet=chef_de_projet
        )
        return redirect('liste_projets')
    chercheurs = Chercheur.objects.all()
    return render(request, 'gestion/projet_form.html', {'chercheurs': chercheurs})

@login_required
def liste_publications(request):
    publications = Publication.objects.all()
    return render(request, 'gestion/publication_list.html', {'publications': publications})

@login_required
def ajouter_publication(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        resume = request.POST.get('resume')
        projet_associe_id = request.POST.get('projet_associe')
        projet_associe = ProjetDeRecherche.objects.get(id=projet_associe_id)
        date_publication = request.POST.get('date_publication')
        Publication.objects.create(
            titre=titre,
            resume=resume,
            projet_associe=projet_associe,
            date_publication=date_publication
        )
        return redirect('liste_publications')
    projets = ProjetDeRecherche.objects.all()
    return render(request, 'gestion/publication_form.html', {'projets': projets})

# Vues basées sur les classes pour l'API (déplacer dans api_views.py)
class ChercheurViewSet(viewsets.ModelViewSet):
    queryset = Chercheur.objects.all()
    serializer_class = ChercheurSerializer

class ProjetDeRechercheViewSet(viewsets.ModelViewSet):
    queryset = ProjetDeRecherche.objects.all()
    serializer_class = ProjetDeRechercheSerializer

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
