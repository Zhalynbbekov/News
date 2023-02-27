# from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Register, News
from .serializers import RegisterSer, HomeSer, LoginSer


class RegisterViews(ModelViewSet):
    serializer_class = RegisterSer
    queryset = Register.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = RegisterSer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class LoginViews(ModelViewSet):
    serializer_class = LoginSer
    queryset = Register.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = LoginSer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data["user_name"]
        # user = authenticate(username=username,
        #                     password=password)
        user = Register.objects.get(user_name=username)
        print(user)
        if user:
            login(request, user)
            return Response(serializer.data, status=200)
        return Response("Error!", status=400)


class HomeViews(ModelViewSet):
    serializer_class = HomeSer
    queryset = News.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = News.objects.all()
        serializer = HomeSer(queryset, many=True)
        return Response(serializer.data)

# Create your views here.
# def main_page(request):
#     register = Register.objects.all()
#
#     return render(request, 'register.html', {'register': register})
#
#
#
# def login(request):
#     login_page = Register.objects.all()
#
#     return render(request, 'login.html', {'login_page': login_page})
#
#
# def home(request):
#     home_page = Register.objects.all()
#     return render(request, 'home.html', {'home_page': home_page})
#
#
# def admin(request):
#     admin_page = Register.objects.all()
#     return render(request, 'admin.html', {'admin_page': admin_page})
