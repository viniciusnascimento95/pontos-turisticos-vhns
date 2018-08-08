from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    #objeto fazendo pesquisa com todos objetos
    #queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)
