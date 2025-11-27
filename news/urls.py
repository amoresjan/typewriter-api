from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, NewsByDateView

router = DefaultRouter()
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('news/<str:date>/', NewsByDateView.as_view(), name='news-by-date'),
    path('news/', NewsByDateView.as_view(), name='news-today'),
    path('', include(router.urls)),
]
