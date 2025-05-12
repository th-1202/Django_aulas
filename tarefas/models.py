from django.db import models

# Create your models here.
class Tarefas(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo