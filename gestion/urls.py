from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ChercheurViewSet, ProjetDeRechercheViewSet, PublicationViewSet
from . import views

router = DefaultRouter()
router.register(r'chercheurs', ChercheurViewSet)
router.register(r'projets', ProjetDeRechercheViewSet)
router.register(r'publications', PublicationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('register/', views.register, name='register'),
    path('chercheurs/', views.liste_chercheurs, name='liste_chercheurs'),
    path('chercheurs/ajouter/', views.ajouter_chercheur, name='ajouter_chercheur'),
    path('projets/', views.liste_projets, name='liste_projets'),
    path('projets/ajouter/', views.ajouter_projet, name='ajouter_projet'),
    path('publications/', views.liste_publications, name='liste_publications'),
    path('publications/ajouter/', views.ajouter_publication, name='ajouter_publication'),
]
