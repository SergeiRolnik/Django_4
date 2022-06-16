from django.shortcuts import render
from articles.models import Article

#query = Article.
for el in Article.objects.all():
    print(el)