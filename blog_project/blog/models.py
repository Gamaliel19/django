from django.db import models

# Create your models here.

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titre

class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.CharField(max_length=100)
    contenu = models.TextField()
    date_commentaire = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.auteur} sur {self.article.titre}"

class Abonne(models.Model):
    email = models.EmailField(unique=True)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

