from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from datetime import datetime
from .models import News
from .serializers import NewsSerializer

class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsByDateView(APIView):
    def get(self, request, date=None):
        if date:
            try:
                # Format: MM-DD-YYYY
                query_date = datetime.strptime(date, '%m-%d-%Y').date()
            except ValueError:
                return Response(
                    {"error": "Invalid date format. Use MM-DD-YYYY."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            query_date = timezone.localdate()

        news_items = News.objects.filter(date=query_date)
        serializer = NewsSerializer(news_items, many=True)
        return Response(serializer.data)
