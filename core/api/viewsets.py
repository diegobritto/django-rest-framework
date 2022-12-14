from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.api.serializers import PontoTuristicoSerializer
from core.models import PontoTuristico

class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = (SearchFilter,)
    search_field = ('nome','descricao','endereco__linha1')
    lookup_field = 'id'

    def get_queryset(self):
        PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
        return Response({'teste':123})
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def denunciar(self, request,pk=None):
        pass

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, id):
        atracoes = request.data['ids']

        ponto = PontoTuristico.objects.get(id=id)

        ponto.atracoes.set(atracoes)

        ponto.save()
        return HttpResponse('ok')