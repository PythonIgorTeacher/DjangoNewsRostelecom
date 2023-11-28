from django.urls import path

from . import views
urlpatterns = [
    path('show', views.index, name='news_index'),
    path('show/<int:id>', views.detail, name='news_detail'),
    path('create', views.create_article, name='create_article')
]
