from rest_framework.serializers import ModelSerializer
from enderecos.models import Endereco
class EnderecoSerializer(ModelSerializer):
    class Meta:
        model=Endereco
        fields =('linha1','linha1','cidade','estado','pais','latitude','longitude')

