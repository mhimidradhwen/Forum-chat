from django.urls import path
from .views import home ,delete_message ,join_username
urlpatterns = [
    path('', home, name="home"),
    path('delete/<int:pk>/',delete_message,name="delete"),
    path('join/',join_username,name='join'),
]
