from django.db import models

class Tarefas(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo