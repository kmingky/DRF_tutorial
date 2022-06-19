from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Article as ArticleModel
from .models import Category as CategoryModel

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
        # data = json.loads(request.body)
        title = request.data.get('title', None)
        category = request.data.get('category', None)
        contents = request.data.get('contents', None)

        category = CategoryModel.objects.get(name = category)

        ArticleModel(title=title, category=category, contents=contents).save()

        return Response({"success": "글쓰기 성공"}, status=status.HTTP_200_OK)
