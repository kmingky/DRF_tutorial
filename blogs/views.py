from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Article as ArticleModel
from .models import Category as CategoryModel

from drf_tutorial.permissions import JoinMoreThanThreeDaysUser, IsAdminOrAuthenticatedReadOnly
from .serializers import ArticleSerializer
from django.utils import timezone
from django.db.models.query_utils import Q

# Create your views here.


class ArticleView(APIView):
    # 로그인된 사용자만 접근가능
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsAdminOrAuthenticatedReadOnly]

    def get(self, request):
        today = timezone.now()
        query = Q(user=request.user) & Q(exposure_start_date__lte=today) & Q(
            exposure_end_date__gte=today)
        articles = ArticleModel.objects.filter(query).order_by("-id")
        print(articles)

        articles_serializer = ArticleSerializer(articles, many=True).data

        return Response(articles_serializer, status=status.HTTP_200_OK)

        # articles = ArticleModel.objects.filter(user=user)
        # titles = [article.title for article in articles]
        # == titles = []
        #  for article in articles:
        #      titles.append(article.title)

        # return Response({"success": "불러오기 성공", "article_list": titles})

    def post(self, request):
        user = request.user
        title = request.data.get('title', "")
        contents = request.data.get('contents', "")
        exposure_start_date = request.data.get('exposure_start_date')
        exposure_end_date = request.data.get('exposure_end_date')

        categorys = request.data.pop('category', [])

        if len(title) <= 5:
            return Response({"error": "제목은 5자 이상이어야 합니다."}, status=status.HTTP_400_BAD_REQUEST)

        if not categorys:
            return Response({"error": "카테고리는 꼭 지정하셔야 합니다."}, status=400)

        if len(contents) <= 20:
            return Response({"error": "내용은 20자 이상이어야 합니다."}, status=status.HTTP_400_BAD_REQUEST)

        article = ArticleModel(
            user=user,
            **request.data
        )

        article.save()
        article.category.add(*categorys)

        return Response({"success": "글쓰기 성공"}, status=status.HTTP_200_OK)
