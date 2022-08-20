from django.urls import path 
from .views import *
urlpatterns = [
    path('',main_api,name='main_api'),
    path('blog-list/',blog_list,name='blog_list'),
    path('blog-detail/<int:id>/',blog_detail,name='blog_detail'),
    path('blog-update/<int:id>/',blog_update,name='blog_upddate'),
    path('blog-delete/<int:id>/',blog_delete,name='blog_delete'),
    path('blog-create/',blog_create,name='blog_create'),
]