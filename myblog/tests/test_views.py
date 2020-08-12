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
        self.article = Article.objects.create(
            title = 'test_title',
            user = self.test_user,
            content = 'test_content'
        )

class TestArticle(CreateUserTestCase):
    def test_article_index(self):
        response = self.client.get(reverse('myblog:Index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['article_list'], ['<Article: test_title>'])

    def test_article_detail(self):
        response = self.client.get(reverse('myblog:Detail', args=(self.article.id,)))
        self.assertContains(response, self.article.content)