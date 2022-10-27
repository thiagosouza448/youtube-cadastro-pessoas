from email.mime import image
from django import forms
from .models import Pessoa, Contato

class PessoaForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )
    image = forms.ImageField(label='Imagem', required=False)
    class Meta:
        model = Pessoa
        fields = ['nome_completo', 'data_nascimento', 'ativa', 'image']

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone']
