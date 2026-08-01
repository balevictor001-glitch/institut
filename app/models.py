from django.db import models

class Promotion(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom


class Etudiant(models.Model):
    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    matricule = models.CharField(max_length=50, unique=True)

    nom = models.CharField(max_length=100)
    postnom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    sexe = models.CharField(
        max_length=1,
        choices=SEXE_CHOICES,
        default='M'
    )
    lieu_naissance = models.CharField(max_length=150, blank=True)
    date_naissance = models.DateField(null=True, blank=True)

    nom_pere = models.CharField(max_length=150, blank=True)
    nom_mere = models.CharField(max_length=150, blank=True)

    adresse = models.TextField(blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    photo = models.ImageField(upload_to='etudiants/', null=True, blank=True)

    promotion = models.ForeignKey(
        Promotion,
        on_delete=models.CASCADE,
        related_name='etudiants'
    )

    actif = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nom} {self.postnom}"