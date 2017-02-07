from django.forms import ModelForm
from apppalestras.models import *

class PalestranteForm(ModelForm):
    class Meta:
        model = Palestrante
        fields = ('nome','dataNascimento','telefone','email','minicurriculo')

class ParticipanteForm(ModelForm):
    class Meta:
        model = Participante
        fields = ('nome', 'dataNascimento', 'telefone', 'email')

class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ('titulo', 'dataInicio', 'dataTermino', 'endereco')
class AtividadeForm(ModelForm):
    #senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    class Meta:
        model = Atividade
        fields = ('titulo', 'duracao', 'tipo', 'participante','palestrante','evento','quantidadeParticipantes')

class EnderecoForm(ModelForm):
    #senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    class Meta:
        model = Endereco
        fields = ('logradouro', 'numero', 'bairro', 'cidade','estado')