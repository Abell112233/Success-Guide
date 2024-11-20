from django import forms
from .models import Curso, Usuario  

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'


class CursosForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'