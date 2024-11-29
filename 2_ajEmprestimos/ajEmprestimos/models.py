from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Endereco(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='enderecos')
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10, null=True, blank=True)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}/{self.estado}"


class TipoEmprestimo(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Emprestimo(models.Model):
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='emprestimos')
    tipo = models.ForeignKey('TipoEmprestimo', on_delete=models.SET_NULL, null=True)
    valor_emprestimo = models.DecimalField(max_digits=10, decimal_places=2)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_pagamento = models.DateField()
    juros = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Empréstimo #{self.id} - Usuário: {self.usuario.nome}"


class HistoricoEmprestimo(models.Model):
    emprestimo = models.ForeignKey('Emprestimo', on_delete=models.CASCADE, related_name='historico')
    data_evento = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()

    def __str__(self):
        return f"Histórico para Empréstimo #{self.emprestimo.id} em {self.data_evento}"

from django.db import models

class Pagamento(models.Model):
    emprestimo = models.ForeignKey('Emprestimo', on_delete=models.CASCADE, related_name='pagamentos')
    data_pagamento = models.DateField()
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pagamento = models.CharField(
        max_length=50, 
        choices=[
            ('boleto', 'Boleto Bancário'),
            ('pix', 'PIX'),
            ('cartao', 'Cartão de Crédito/Débito'),
            ('transferencia', 'Transferência Bancária'),
        ],
        default='pix'
    )
    status = models.CharField(
        max_length=20, 
        choices=[
            ('pendente', 'Pendente'),
            ('aprovado', 'Aprovado'),
            ('rejeitado', 'Rejeitado')
        ],
        default='pendente'
    )

    def __str__(self):
        return f"Pagamento #{self.id} - Empréstimo {self.emprestimo.id} - Status: {self.status}"
