from urllib import request, response
from rest_framework import serializers
from .models import User as UserModel
from .models import UserProfile as UserProfileModel
from .models import Hobby as HobbyModel
from blogs.models import Article as ArticleModel
from blogs.models import Comment as CommentModel

# serializer에 추가로 로그인 한 사용자의 게시글, 댓글을 리턴해주는 기능을 구현해주세요
# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CommentModel
#         fields = ["user", "contents"]


class ArticleSerializer(serializers.ModelSerializer):
    # comment = CommentSerializer()

    class Meta:
        model = ArticleModel
        fields = ["title", "category", "contents", "comment"]


# serializer를 활용해 로그인 한 사용자의 기본 정보와 상세 정보를 리턴해 주는 기능을 만들어주세요
class HobbyModelSerializer(serializers.ModelSerializer):
    same_hobby_users = serializers.SerializerMethodField()
    def get_same_hobby_users(self, obj):
        # user_list = []
        # for user_profile in obj.userprofile_set.all():
        #     user_list.append(user_profile.user.fullname)
        return [user_profile.user.fullname for user_profile in obj.userprofile_set.all()]

    class Meta:
        model = HobbyModel
        fields = ["name", "same_hobby_users"]


class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbyModelSerializer(many=True)

    class Meta:
        model = UserProfileModel
        fields = ["gender", "birthday", "hobby"]


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    article = ArticleSerializer(many=True)

    class Meta:
        model = UserModel
        fields = ["username", "fullname", "join_date", "userprofile", "article"]

