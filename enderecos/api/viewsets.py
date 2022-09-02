from rest_framework.viewsets import ModelViewSet
from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco

class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer