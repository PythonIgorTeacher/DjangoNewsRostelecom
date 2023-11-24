from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import News, Product
from django.db import connection, reset_queries
from news.models import Article
def index(request):
    # Примеры Values values_list
    # all_news = Article.objects.all().values('author','title')
    # for a in all_news:
    #     print(a['author'], a['title'])
    # all_news = Article.objects.all().values_list('title', flat=True)
    # print(all_news)
    # all_news = Article.objects.all().values_list('title')
    # print(all_news)
    # for a in all_news:
    #     print(a)
    # #по-старому
    # article = Article.objects.get(id=1)
    # print(article.author.username)
    # #Select_related O2O, O2M:
    # article = Article.objects.select_related('author').get(id=1)
    # print(article.author.username)
    #prefertch_related M2M
    # articles = Article.objects.all()
    # for a in articles:
    #     print(a.title, a.tags.all())
    # articles = Article.objects.prefetch_related('tags').all()
    from django.db.models import Count, Avg, Max
    from django.contrib.auth.models import User
    # #пример аннотирования и агрегации:
    # count_articles = User.objects.annotate(Count('article',distinct=True))
    # print(count_articles)
    # for user in count_articles:
    #     print(user, user.article__count)
    # пример аннотирования и агрегации:
    # count_articles = User.objects.annotate(Count('article', distinct=True)).aggregate(Avg('article__count'))
    # print(count_articles)
    # пример аннотирования и агрегации:
    max_article_count_user = User.objects.annotate(Count('article', distinct=True)).order_by('-article__count').first()
    print(max_article_count_user)
    max_article_count =  User.objects.annotate(Count('article', distinct=True)).aggregate(Max('article__count'))
    max_article_count_user2 = User.objects.annotate(Count('article', distinct=True)).filter(article__count__exact=max_article_count['article__count__max'])
    print(max_article_count_user2)
    return render(request,'main/index.html')

def news(request):
    return render(request,'main/news.html')

def examples(request):
    # value = -10
    # n1 = News('Новость 1','Текст 1','07.11.23')
    # n2 = News('Новость 2','Текст 2','01.11.23')
    # l = [n1, n2]
    # d = {1: 'один', 'Два': 2}
    #
    # context = {'title': 'Страница главная',
    #            'Header1': 'Заголовок страницы',
    #            'numbers': l,
    #            'dictionary': d,
    #            'value':value,
    #            }
    # context['пример']= 'Example'

    if request.method == 'POST':
        print('Получили post-Запрос!')
        print(request.POST)
        title = request.POST.get('title')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        new_product = Product(title,float(price),int(quantity))
        print('Создан товар:',new_product.title, 'Общая сумма:',new_product.amount())
    else:
        print('Получили get-Запрос!')
    water = Product('Добрый-минералка', 43, 2)
    chocolate = Product('Шоколадка', 80, 1)

    colors = ['red','blue','golden','black']
    context = {
        'colors':colors,
        'water': water,
        'chocolate':chocolate,
    }
    return render(request,'main/examples.html', context)

def get_demo(request,a,operation,b):
    match operation:
        case 'plus':
            result = int(a)+ int(b)
        case 'minus':
            result = int(a) - int(b)
        case 'multiply':
             result = int(a) * int(b)
        case 'divide':
            result = int(a) / int(b)
        case _:
            return HttpResponse(f'Неверная команда')
    return HttpResponse(f'Вы ввели: {a} и {b} <br>Результат {operation}: {result}')


def about(request):
    return HttpResponse('<h1> о нас </h1>')


def contacts(request):
    return HttpResponse('<h1> контакты </h1>')


def sidebar(request):
    return render(request,'main/sidebar.html')


def custom_404(request, exception):
    # return render(request,'main/sidebar.html')
    return HttpResponse(f'Ой-ёй-ёй! Какая жалость!:{exception}')