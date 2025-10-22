from django.db import models

# Create your models here.
# stations/models.py
from django.db import models

class Station(models.Model):
    name = models.CharField("Nom de la station", max_length=200)
    location = models.CharField("Localisation", max_length=200)
    status = models.CharField(
        "Statut",
        max_length=20,
        choices=[('disponible', 'Disponible'), ('indisponible', 'Indisponible')],
        default='disponible'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.status})"
