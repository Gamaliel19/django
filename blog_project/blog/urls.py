from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),  # Page d'accueil
    path('article/<int:article_id>/', views.detail_article, name='detail_article'),  # Page de détail
    path('article/<int:article_id>/aimer/', views.aimer_article, name='aimer_article'),
    path('article/<int:article_id>/commenter/', views.ajouter_commentaire, name='ajouter_commentaire'),
    path('newsletter/abonner/', views.abonnement_newsletter, name='abonnement_newsletter'),

]
