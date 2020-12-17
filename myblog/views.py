from django.views import generic
from accounts.models import CustomUser
from .models import Article
from .models import Tag


class ArticleListView(generic.ListView):
    model = Article
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_list = CustomUser.objects.order_by('-username')

        context.update({
            'user_list': user_list,
        })
        return context

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


class TagListView(generic.ListView):
    model = Tag
    template_name = 'tag_index.html'

    def get_queryset(self):
        tag = Tag.objects.all().order_by('-name')
        return tag


class ArticleByTagListView(generic.ListView):
    model = Article
    template_name = 'article_by_tag_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('pk')
        article_list = Article.objects.filter(tags__in=[tag_id]).order_by('-created_at')
        tag = Tag.objects.filter(id=tag_id)
        tag_name = tag[0].name if tag and tag[0] else ''
        context.update({
            'article_list': article_list,
            'tag_name': tag_name
        })
        return context
