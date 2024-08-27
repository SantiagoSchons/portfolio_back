from rest_framework.serializers import ModelSerializer
from port.models import Certificacoes

class CertificacoesSerializers(ModelSerializer):
    class Meta:
        model = Certificacoes
        fields = "__all__"