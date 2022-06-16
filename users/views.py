from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response


# Create your views here.
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