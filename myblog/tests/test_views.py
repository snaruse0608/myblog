from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from ..models import Article

class CreateUserTestCase(TestCase):
    def setUp(self):
        self.password = 'admin'
        self.test_user = get_user_model().objects.create_user(
            username='testUser',
            email='testUser@testUser.com',
            password=self.password)

class TestArticle(CreateUserTestCase):
    def test_article_index(self):
        self.article = Article.objects.create(
            title = 'test_title',
            user = self.test_user,
            content = 'test_content'
        )
        response = self.client.get(reverse('myblog:Index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['article_list'], ['<Article: test_title>'])

    def test_article_detail(self):
        self.article = Article.objects.create(
            title = 'test_title',
            user = self.test_user,
            content = 'test_content'
        )
        # 閲覧数が0件を確認
        self.assertEqual(self.article.views, 0)

        response = self.client.get(reverse('myblog:Detail', args=(self.article.id,)))
        self.assertContains(response, self.article.content)
        
        # 閲覧数が1件を確認
        article_view_check = Article.objects.get(id=self.article.id)
        self.assertEqual(article_view_check.views, 1)


class TestArticleError(CreateUserTestCase):
    def test_article_index_error(self):
        response = self.client.get(reverse('myblog:Index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ブログがありません')

    def test_article_detail_error(self):
        article = Article(
            title = 'test_title',
            user = self.test_user,
            content = 'test_content'
        )
        response = self.client.get(reverse('myblog:Detail', args=(article.id,)))
        self.assertEqual(response.status_code, 404)