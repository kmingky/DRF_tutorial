from rest_framework import serializers
from .models import User as UserModel
from .models import UserProfile as UserProfileModel
from .models import Hobby as HobbyModel

from blogs.serializers import ArticleSerializer, CommentSerializer


# serializer를 활용해 로그인 한 사용자의 기본 정보와 상세 정보를 리턴해 주는 기능을 만들어주세요
class HobbyModelSerializer(serializers.ModelSerializer):
    same_hobby_users = serializers.SerializerMethodField()
    def get_same_hobby_users(self, obj):
        user = self.context["request"].user
        print(user)
        # user_list = []
        # for user_profile in obj.userprofile_set.all():
        #     user_list.append(user_profile.user.fullname)
        return [user_profile.user.fullname for user_profile in obj.userprofile_set.exclude(user=user)]

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
    articles = ArticleSerializer(many=True, source='article_set')
    comments = CommentSerializer(many=True, source='comment_set')

    class Meta:
        model = UserModel
        fields = ["username", "fullname", "join_date", "userprofile", "articles", "comments"]




# 회원가입을 위한 시리얼라이저
class UserJoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user