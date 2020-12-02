from django.urls import path
from . import views

app_name = 'myblog'
urlpatterns = [
    path('', views.ArticleListView.as_view(), name='Index'),
    path('detail/<pk>/', views.ArticleDetailView.as_view(), name='Detail'),
    path('tag', views.TagListView.as_view(), name='TagIndex'),
    path('article/tag/<pk>/', views.ArticleByTagListView.as_view(), name='ArticleByTagIndex')
]