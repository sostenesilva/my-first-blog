from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    foto = models.FileField(upload_to="media/capa/", blank=True, null=True)
    video = models.CharField(max_length=50, blank=True, null=True)
    letra = models.TextField()
    cifra = models.TextField(max_length=2000, default='Cifra indisponível até o momento.')
    creditos = models.TextField(max_length=2000, default="Créditos:")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
