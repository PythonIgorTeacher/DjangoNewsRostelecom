from django.shortcuts import render, HttpResponse
from .models import *

# def news(request):
#     return render(request,'news/news.html')

def index(request):
    # print(request.user.id)
    # # articles = Article.objects.filter(author=request.user.id)
    # print(articles)
    article = Article.objects.filter(author=request.user)
    # for t in article.tags.all():
    #     print(t.title)
    user_list = User.objects.all()
    for user in user_list:
        print(Article.objects.filter(author=user))
    print(user_list)
    print('!!!!!!!!!!!!!!!!!!!!!!!!Результаты',article)
    # print(article.tags.all())
    # tag = Tag.objects.filter(title='IT')[0]
    # tagged_news = Article.objects.filter(tags=tag)
    # print(tagged_news)

    context = {'article':article}
    return render(request,'news/index.html',context)

def detail(request,id):
    # article = Article.objects.filter(id=id)[0]
    # print(article,type(article))
    #пример создания новости
    # author = User.objects.get(id=request.user.id)
    # article = Article(author=author,title='Заголовок1',
    #                   anouncement='Анонс', text='текст')
    # article.save()

    #пример итерирования по объектам QuerySet
    articles = Article.objects.all()
    s=''
    for article in articles:
        s+=f'<h1>{article.title}</h1><br>'
    return HttpResponse(s)

