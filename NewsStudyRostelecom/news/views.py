from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from .models import *
from django.db import connection, reset_queries
from django.views.generic import DetailView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from .forms import *
#человек не аутентифицирован - отправляем на страницу другую

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'news/news_detail.html'
    context_object_name = 'article'

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'news/create_article.html'
    fields = ['title','anouncement','text','tags']

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('news_index') #именованная ссылка или абсолютную
    template_name = 'news/delete_article.html'



@login_required(login_url="/")
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
    articles = Article.objects.all()
    a = articles.first()
    categories = Article.categories
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
    context = {'articles': articles, 'author_list':author_list,'selected':selected,'categories':categories, }
    return render(request,'news/news_list.html',context)

# def detail(request,id):
#     #пример итерирования по объектам QuerySet
#     articles = Article.objects.all()
#     s=''
#     for article in articles:
#         s+=f'<h1>{article.title}</h1><br>'
#     return HttpResponse(s)

