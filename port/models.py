from django.db import models

# Create your models here.

class Certificacoes(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    image = models.URLField(max_length=255)

    def __str__(self) -> str:
        return self.title    
