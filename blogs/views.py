from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Article as ArticleModel
from .models import Category as CategoryModel

from drf_tutorial.permissions import MyCustomPermission

# Create your views here.
class ArticleView(APIView):
    # 로그인된 사용자만 접근가능
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        user = request.user

        articles = ArticleModel.objects.filter(user=user)
        titles = [article.title for article in articles]
        # == titles = []
        #  for article in articles:
        #      titles.append(article.title)

        return Response({"success": "불러오기 성공", "article_list": titles})

    
    def post(self, request):
        permission_classes = [MyCustomPermission]
        user = request.user
        title = request.data.get('title', "")
        categorys = request.data.get('category', [])
        contents = request.data.get('contents', "")

        if len(title) <= 5:
            return Response({"error": "제목은 5자 이상이어야 합니다."}, status=status.HTTP_400_BAD_REQUEST)

        if not categorys:
            return Response({"error": "카테고리는 꼭 지정하셔야 합니다."}, status=400)

        if len(contents) <= 20:
            return Response({"error": "내용은 20자 이상이어야 합니다."}, status=status.HTTP_400_BAD_REQUEST)


        article = ArticleModel(
            user=user,
            title=title,
            contents=contents
        )

        article.save()
        article.category.add(*categorys)

        return Response({"success": "글쓰기 성공"}, status=status.HTTP_200_OK)
