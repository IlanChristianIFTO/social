from django.shortcuts import render, redirect, get_object_or_404
from .models import Postagem
from .forms import PostagemForm, ComentarioForm


# Função de index - Exibir as postagens
def index(request):
    postagem = Postagem.objects.order_by('-data_postagem')
    return render(request, 'social/index.html', {'postagens': postagem})


# Criar nova postagem
def nova_postagem(request):
    if request.method == 'POST':
        form = PostagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostagemForm()
    return render(request, 'social/nova_postagem.html', {'form': form})


# Função para curtir postagem
def curtir_postagem(request, postagem_id):
    postagem = get_object_or_404(Postagem, id=postagem_id)
    postagem.curtidas += 1
    postagem.save()
    return redirect('index')


# Função para descurtir postagem
def descurtir_postagem(request, postagem_id):
    postagem = get_object_or_404(Postagem, id=postagem_id)
    postagem.descurtidas += 1
    postagem.save()
    return redirect('index')


# Função para comentar em uma postagem
def comentar(request, postagem_id):
    postagem = get_object_or_404(Postagem, id=postagem_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.postagem = postagem
            comentario.save()
            return redirect('index')
    else:
        form = ComentarioForm()

    return render(request, 'social/comentar.html', {'form': form, 'postagem': postagem})
