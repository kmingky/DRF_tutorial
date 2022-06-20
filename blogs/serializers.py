from unicodedata import category
from rest_framework import serializers
from users.models import User as UserModel
from users.models import UserProfile as UserProfileModel
from users.models import Hobby as HobbyModel
from .models import Article as ArticleModel
from .models import Comment as CommentModel

# serializer에 추가로 로그인 한 사용자의 게시글, 댓글을 리턴해주는 기능을 구현해주세요
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = CommentModel
        fields = ["user", "contents"]


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, source="comment_set")

    def get_category(self, obj):
        return [category.name for category in obj.category.all()]

    class Meta:
        model = ArticleModel
        fields = ["title", "category", "contents", "comments"]

