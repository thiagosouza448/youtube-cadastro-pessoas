from django import forms
from django.forms import fields, models
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome_completo', 'data_nascimento', 'ativa']