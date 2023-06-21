

from django.shortcuts import render
from . models import Article, Comment


def index(request):
    list = Article.objects.order_by('date',)
    return render(request, 'articles/list.html',{'list':list})

def number(request, article_id):
    pass
