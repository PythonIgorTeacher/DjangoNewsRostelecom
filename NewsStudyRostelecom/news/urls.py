from django.urls import path

from . import views
urlpatterns = [
    path('show', views.index, name='news'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('show/<int:pk>', views.ArticleDetailView.as_view(), name='news_detail'),
    path('update/<int:pk>', views.ArticleUpdateView.as_view(), name='news_update'),
    path('delete/<int:pk>', views.ArticleDeleteView.as_view(), name='news_delete'),
    path('create', views.create_article, name='create_article'),
    # path('pagination',views.pagination,name='pagination'),
]

