from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    # Add the remaining URL path configurations here
    path('home/', views.home, name="home"),
    path('menu/', views.menu, name="menu"),
       #<> - oznaka za ocekivani input
       #menu_item je klikable
    path('menu/<int:pk>/', views.menu_item_detail, name='menu_item'),
]