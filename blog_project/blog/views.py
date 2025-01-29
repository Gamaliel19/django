from django.shortcuts import render, get_object_or_404
from .models import Article, Commentaire, Abonne
from django.http import JsonResponse


# Vue pour la liste des articles
def liste_articles(request):
    articles = Article.objects.order_by('-date_publication')  # Trier par date décroissante
    return render(request, 'liste_articles.html', {'articles': articles})

# Vue pour un article détaillé
def detail_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)  # Récupérer l'article ou retourner 404
    return render(request, 'detail_article.html', {'article': article})

# Vue pour permettre d'incremmenter les "J'aimes"
def aimer_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.likes += 1
    article.save()
    return JsonResponse({'likes': article.likes})  # Retourne le nouveau nombre de likes

#Vue pour permettre l'ajouter d'un commentaire à un article 
def ajouter_commentaire(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, id=article_id)
        auteur = request.POST.get('auteur')
        contenu = request.POST.get('contenu')
        Commentaire.objects.create(article=article, auteur=auteur, contenu=contenu)
        return redirect('detail_article', article_id=article.id)

#Vue pour permettre aux visiteur de s'abonner
def abonnement_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not Abonne.objects.filter(email=email).exists():
            Abonne.objects.create(email=email)
        return JsonResponse({'message': 'Abonnement réussi!'})

