from rest_framework import serializers
from .models import Usuario, Endereco, TipoEmprestimo, Emprestimo, HistoricoEmprestimo, Pagamento

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'sobrenome', 'data_nascimento', 'cpf', 'email']


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'usuario', 'rua', 'numero', 'complemento', 'cidade', 'estado', 'cep']
        
        
class TipoEmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEmprestimo
        fields = ['id', 'descricao']
        
class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = [
            'id', 
            'usuario', 
            'tipo', 
            'valor_emprestimo', 
            'data_emprestimo', 
            'data_pagamento', 
            'juros'
        ]
        
class HistoricoEmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoEmprestimo
        fields = ['id', 'emprestimo', 'data_evento', 'descricao']
        
        
class UsuarioDetailSerializer(serializers.ModelSerializer):
    enderecos = EnderecoSerializer(many=True, read_only=True, source='enderecos')

    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'sobrenome', 'data_nascimento', 'cpf', 'email', 'enderecos']


class EmprestimoDetailSerializer(serializers.ModelSerializer):
    historico = HistoricoEmprestimoSerializer(many=True, read_only=True, source='historico')

    class Meta:
        model = Emprestimo
        fields = [
            'id', 
            'usuario', 
            'tipo', 
            'valor_emprestimo', 
            'data_emprestimo', 
            'data_pagamento', 
            'juros', 
            'historico'
        ]


class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ['id', 'emprestimo', 'data_pagamento', 'valor_pago', 'metodo_pagamento', 'status']
        read_only_fields = ['id']
    
    
