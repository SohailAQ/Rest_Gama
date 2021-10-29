from django.conf import settings
from rest_auth.registration.serializers import RegisterSerializer as RestAuthRegisterSerializer
from rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer
from rest_framework import serializers

from users.models import CustomUser


# class CustomUserRegisterSerializer(RestAuthRegisterSerializer):
#     def get_email_options(self):
#         return {
#             'html_email_template_name': 'registration/user_registration_confirm_email.html',
#         }


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'profile', 'dob', 'date_joined', 'last_login')
        read_only_fields = ('id', 'email', 'date_joined', 'last_login',)


class LoginSerializer(RestAuthLoginSerializer):
    username = None
