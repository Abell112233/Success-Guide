from django import forms
from .models import Curso 

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