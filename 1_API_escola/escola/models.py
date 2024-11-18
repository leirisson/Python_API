from django.db import models

'''

ID
Nome
E-mail
CPF
Máxima 11 caracteres
Data de nascimento
Número de celular
Máximo de 14 caracteres 

'''
class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    numero_celular = models.CharField(max_length=14)

    def __str__(self):
        return self.nome
    