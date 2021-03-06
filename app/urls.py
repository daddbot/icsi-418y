from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search, name='search'),
    path('search/acquire/', views.acquire, name='acquire'),
    path('results/', views.results, name='results'),
]