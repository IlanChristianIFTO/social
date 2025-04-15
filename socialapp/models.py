from django.db import models

class Postagem(models.Model):
    titulo = models.CharField(max_length=255)
    nome_usuario = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)
    curtidas = models.PositiveIntegerField(default=0)
    descurtidas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, related_name='comentarios')
    nome_usuario = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.nome_usuario} em {self.form.titulo}"