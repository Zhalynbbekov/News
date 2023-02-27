from rest_framework import serializers

from news.models import Register, News


class RegisterSer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'


class LoginSer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['user_name', 'password']


class HomeSer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
