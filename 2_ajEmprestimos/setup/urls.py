from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ajEmprestimos.views import (
    UsuarioViewSet,
    EnderecoViewSet,
    TipoEmprestimoViewSet,
    EmprestimoViewSet,
    HistoricoEmprestimoViewSet,
    PagamentoViewSet
)

router = DefaultRouter()

router.register('usuarios', UsuarioViewSet, basename='usuarios')
router.register('enderecos', EnderecoViewSet, basename='enderecos')
router.register('tipos-emprestimos', TipoEmprestimoViewSet, basename='tipos-emprestimos')
router.register('emprestimos', EmprestimoViewSet, basename='emprestimos')
router.register('historico-emprestimo', HistoricoEmprestimoViewSet, basename= 'historico-emprestimo')
router.register('pagamento', PagamentoViewSet, basename="pagamento")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
