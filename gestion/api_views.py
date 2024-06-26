from rest_framework import viewsets
from .models import Chercheur, ProjetDeRecherche, Publication
from .serializers import ChercheurSerializer, ProjetDeRechercheSerializer, PublicationSerializer

class ChercheurViewSet(viewsets.ModelViewSet):
    queryset = Chercheur.objects.all()
    serializer_class = ChercheurSerializer

class ProjetDeRechercheViewSet(viewsets.ModelViewSet):
    queryset = ProjetDeRecherche.objects.all()
    serializer_class = ProjetDeRechercheSerializer

class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
