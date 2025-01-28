from django.shortcuts import render
from .models import Article

def liste_articles(request):
    articles = Article.objects.all()  # Récupérer tous les articles
    return render(request, 'liste_articles.html', {'articles': articles})

