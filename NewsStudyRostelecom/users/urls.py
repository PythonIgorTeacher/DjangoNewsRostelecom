from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    path('', views.index, name='user_index'),
    path('contact_page',views.contact_page,name='contact_page'),
    path('registration',views.registration,name='registration'),
    path('login', auth_views.LoginView.as_view(
        template_name='users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(
        template_name='users/logout.html'), name='logout'),
    path('profile',views.profile,name='profile'),
    path('profile/update', views.profile_update, name='profile_update'),
    path('profile/delete', views.profile_delete, name='profile_delete'),
    path('password', views.password_update, name='password'),
    path('favorites/<int:id>', views.add_to_favorites, name='favorites'),
    path('mynewslist',views.my_news_list,name='my_news_list'),
    path('profile/favorites',views.my_favorites_list,name='my_favorites_list')
]
