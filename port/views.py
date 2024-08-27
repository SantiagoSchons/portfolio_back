from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from port.serializers import CertificacoesSerializers
from port.models import Certificacoes
# Create your views here.

class CertificacoesViewSet(ModelViewSet):
    queryset = Certificacoes.objects.all()
    serializer_class = CertificacoesSerializers
