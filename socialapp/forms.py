from django import forms
from .models import Postagem, Comentario


class PostagemForm(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = ['nome_usuario', 'titulo', 'conteudo']
        widgets = {
            'nome_usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'conteudo': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome_usuario', 'conteudo']