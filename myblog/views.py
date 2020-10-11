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

    # 取得した記事の閲覧数を+1する
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = context.get("object")
        article.views += 1
        article.save()
        return context