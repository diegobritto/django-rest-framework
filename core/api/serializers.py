from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao
from enderecos.api.serializers import EnderecoSerializer
from core.models import PontoTuristico
class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True, read_only=True)
    endereco = EnderecoSerializer(read_only=True)
    descricao_completa = SerializerMethodField()
    class Meta:
        model=PontoTuristico
        fields =('id','nome','descricao','comentarios','avaliacoes','avaliacoes','descricao_completa')
        read_only_fields = ('comentarios','avaliacoes')

    def cria_atracoes(self,atracoes,ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)
    def cria_endereco(self,endereco,ponto):
        en = Atracao.objects.create(**endereco)
        ponto.enderecos.add(en)
    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del  validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)
        self.cria_endereco(endereco,ponto)
        return ponto
    def get_descricao_completa(self,obj):
        return '%s - %s' % (obj.nome,obj.descricao)

