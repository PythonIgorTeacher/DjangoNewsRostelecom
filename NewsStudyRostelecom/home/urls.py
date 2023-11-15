from django.urls import path

from . import views
urlpatterns = [
    path('demoform/',views.demoform),
    path('showlastmodel/',views.showlastmodel),
    path('', views.index, name='demo'),
]
