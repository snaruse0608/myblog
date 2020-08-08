from django.urls import path
from . import views

app_name = 'myblog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='Index'),
]