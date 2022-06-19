from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth.hashers import make_password

from .models import User


# Create your views here.
class JoinView(APIView):
    permission_classes = [permissions.AllowAny]
    # 회원 가입
    def post(self, request):
        # data = json.loads(request.body)
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        email = request.data.get('email', None)
        fullname = request.data.get('fullname', None)

        User.objects.create(
        username=username,
        password=make_password(password),
        email=email,
        fullname=fullname
        )

        return Response({"success": "회원가입 성공"}, status=status.HTTP_200_OK)

class UserAPIView(APIView):
    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)

        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."})
        
        login(request, user)
        return Response({"success": "로그인 성공"})
    #== else:
    #   login(request, user)
    #   return Response({"success": "로그인 성공"})

    def delete(self, request):
        logout(request)
        return Response({"success": "로그아웃 성공"})