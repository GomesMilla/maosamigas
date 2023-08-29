from django.urls import path
from django.contrib.auth import views as auth_views

from django.views.generic import TemplateView
from .views import PedirDoacaoCreateView, SolicitacoesListView, SolicitacaoDetailView, IntroductionView, SolicitacoesPorCategoria, PedirDoacaolUpdate
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("objetivo/", TemplateView.as_view(template_name="presentation/objetivo.html"), name="objetivo"),
    path("introducao/", IntroductionView.as_view(), name="introducao"),
    path("pedir-doacao/", login_required(PedirDoacaoCreateView.as_view()), name="pedir_doacao"),
    path("solicitacoes/", SolicitacoesListView.as_view(), name="solicitacoes"),
    path("solicitacoes-por-categoria/<int:pk>", SolicitacoesPorCategoria.as_view(), name="solicitacoes_por_categoria"),
    path("solicitacao/<int:pk>/edit", PedirDoacaolUpdate.as_view(), name="editar_solicitacao"),
    path("ver-solicitacao/<int:pk>", SolicitacaoDetailView.as_view(), name="ver_solicitacao"),
]
