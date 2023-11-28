from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.db import connection, reset_queries
# def news(request):
#     return render(request,'news/news.html')

from .forms import *
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            current_user = request.user
            if current_user.id != None: #проверили что не аноним

                new_article = form.save(commit=False)
                new_article.author = current_user
                new_article.save() #сохраняем в БД
                form = ArticleForm()

                return redirect('news_index')
    else:
        form = ArticleForm()
    return render(request,'news/create_article.html', {'form':form})


def index(request):
    #пример применения пользовательского менджера
    articles = Article.published.all()
    context={'today_articles': articles}
    author_list = User.objects.all()
    selected = 0
    if request.method=="POST":
        print(request.POST)
        selected = int(request.POST.get('author_filter'))
        if selected == 0:
            articles = Article.objects.all()
        else:
            articles = Article.objects.filter(author=selected)
        print(connection.queries)
    else:
        articles = Article.objects.all()
    context = {'articles': articles, 'author_list':author_list,'selected':selected }
    return render(request,'news/news_list.html',context)

def detail(request,id):
    #пример итерирования по объектам QuerySet
    articles = Article.objects.all()
    s=''
    for article in articles:
        s+=f'<h1>{article.title}</h1><br>'
    return HttpResponse(s)

