from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('update_server/',views.update_server,name='update_server'),
    path('examples/',views.examples,name='examples'),
    path('calc/<int:a>/<slug:operation>/<int:b>',views.get_demo),
    # 127.0.0.1:8000/calc/10/power/2
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contact'),
    path('sidebar/', views.sidebar),

]
