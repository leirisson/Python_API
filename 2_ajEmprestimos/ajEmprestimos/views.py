from rest_framework import viewsets
from .models import Usuario, Endereco, TipoEmprestimo, Emprestimo, HistoricoEmprestimo, Pagamento
from .serializers import (
    UsuarioSerializer,
    EnderecoSerializer,
    TipoEmprestimoSerializer,
    EmprestimoSerializer,
    HistoricoEmprestimoSerializer,
    PagamentoSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    
class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class TipoEmprestimoViewSet(viewsets.ModelViewSet):
    queryset = TipoEmprestimo.objects.all()
    serializer_class = TipoEmprestimoSerializer

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer



class HistoricoEmprestimoViewSet(viewsets.ModelViewSet):
    queryset = HistoricoEmprestimo.objects.all()
    serializer_class = HistoricoEmprestimoSerializer

class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
