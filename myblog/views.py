from django.views import generic
from .models import Article

class ArticleListView(generic.ListView):
    model = Article
    template_name = 'index.html'

    def get_queryset(self):
        articles = Article.objects.all().order_by('-created_at')
        return articles

class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'detail.html'