from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import News
from datetime import date

class NewsModelTest(TestCase):
    def test_create_news(self):
        news = News.objects.create(
            title="Test News",
            content="Test Content",
            author="Test Author",
            source="Test Source",
            date=date.today()
        )
        self.assertEqual(news.title, "Test News")
        self.assertEqual(str(news), "Test News")

class NewsAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.news = News.objects.create(
            title="API News",
            content="API Content",
            author="API Author",
            source="API Source",
            date=date.today()
        )

    def test_get_news_list(self):
        response = self.client.get('/api/news/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "API News")
