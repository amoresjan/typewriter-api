from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, NewsByDateView, GenerateNewsView

router = DefaultRouter()
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('news/<str:date>/', NewsByDateView.as_view(), name='news-by-date'),
    path('news/', NewsByDateView.as_view(), name='news-today'),
    path('generate/', GenerateNewsView.as_view(), name='news-generate'),
    path('', include(router.urls)),
]
