from django import forms
from .models import Curso, Usuario
from django.contrib.auth.forms import UserCreationForm

class CursosForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'input-text js-input',}),
            'carga_horaria': forms.NumberInput(attrs={'class': 'input-text js-input'}),
            'endereco': forms.TextInput(attrs={'class': 'input-text js-input'}),
            'area': forms.Select(attrs={'class': 'input-text js-input'}),
            'link': forms.URLInput(attrs={'class': 'input-text js-input'}),
        }

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'telefone', 'password1', 'password2')

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'input-text js-input'}),
            'telefone': forms.TextInput(attrs={'class': 'input-text js-input'}),
        }

class FiltroForm(forms.Form):
    nome = forms.CharField(max_length=150, required=False,
                           label='Título',
                           widget=forms.TextInput(attrs={'placeholder': 'Nome', 'class': 'form-control'}))