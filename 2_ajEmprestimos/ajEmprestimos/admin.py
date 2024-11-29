from django.contrib import admin

from ajEmprestimos.models import Usuario, Endereco, TipoEmprestimo, Emprestimo, HistoricoEmprestimo, Pagamento


class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'data_nascimento', 'cpf', 'email')
    list_display_links = ('id', 'nome')
    list_per_page = 20
    search_fields = ('id', 'nome',)
    
admin.site.register(Usuario, Usuarios)

class Enderecos(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'rua', 'numero', 'complemento', 'cidade', 'estado', 'cep')
    list_display_links = ('id', 'usuario')
    list_per_page = 20
    search_fields = ('id', 'usuario')
    
admin.site.register(Endereco, Enderecos)

class TipoEmprestimos(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    list_display_links = ('id',)
    list_per_page = 20
    search_fields = ('id', 'descricao')

admin.site.register(TipoEmprestimo, TipoEmprestimos)

class Emprestimos(admin.ModelAdmin):
    list_display = ('id', 'usuario','tipo','valor_emprestimo','data_emprestimo', 'data_pagamento','juros')
    list_display_links = ('id', 'usuario',)
    list_per_page = 20
    search_fields = ('id', 'usuario')

admin.site.register(Emprestimo, Emprestimos)

class HistoricoEmprestimos(admin.ModelAdmin):
    list_display = ('id', 'emprestimo', 'data_evento', 'descricao')
    list_display_links = ('id', 'emprestimo',)
    list_per_page = 20
    search_fields = ('id', 'emprestimo')

admin.site.register(HistoricoEmprestimo, HistoricoEmprestimos)

class Pagamentos(admin.ModelAdmin):
    list_display = ('id', 'emprestimo', 'data_pagamento', 'valor_pago', 'metodo_pagamento', 'status')
    list_display_links = ('id',)
    list_per_page = 20
    search_fields = ('id', 'emprestimo')
admin.site.register(Pagamento, Pagamentos)
