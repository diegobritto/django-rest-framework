from rest_framework.viewsets import ModelViewSet
from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao

class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer