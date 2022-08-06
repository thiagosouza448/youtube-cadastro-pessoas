from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import PessoaSerializer

from pessoa.models import Pessoa


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all().order_by('nome_completo')
    serializer_class = PessoaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        pessoas = super().get_queryset()
        pessoas = pessoas.filter(usuario=self.request.user)
        return pessoas
    