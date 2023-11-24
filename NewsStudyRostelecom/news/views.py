from django.shortcuts import render, HttpResponse
from .models import *

# def news(request):
#     return render(request,'news/news.html')

def index(request):
    author_list = User.objects.all()
    selected = 0
    if request.method=="POST":
        selected = int(request.POST.get('author_filter'))
        if  selected == 0:
            articles = Article.objects.all()

        else:
            articles = Article.objects.filter(author=selected)
    else:
        articles = Article.objects.all()
    context = {'articles':articles, 'author_list':author_list,'selected':selected }
    return render(request,'news/news_list.html',context)

def detail(request,id):
    #пример итерирования по объектам QuerySet
    articles = Article.objects.all()
    s=''
    for article in articles:
        s+=f'<h1>{article.title}</h1><br>'
    return HttpResponse(s)

