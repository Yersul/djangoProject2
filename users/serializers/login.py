from rest_framework.exceptions import ValidationError
from django.contrib.auth import login, logout
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from users.verifications import send_sms_code, is_code_correct
from users.models import CustomUser


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12, required=True)
    otp = serializers.CharField(max_length=4, required=False)
    refresh = serializers.CharField(max_length=100, required=False)

    class Meta:
        fields = {
            'phone',
            'otp',
            'refresh'
        }

    def validate(self, attrs):
        attrs['otp_check'] = False

        if 'phone' in attrs.keys():
            user = CustomUser.objects.filter(phone=attrs['phone']).first()
            if not user:
                user = CustomUser.objects.create_user(phone=attrs['phone'])
            attrs['user'] = user
        else:
            raise ValidationError('"phone" field not found, try again')

        if 'otp' in attrs.keys():
            check = is_code_correct(attrs['phone'], attrs['otp'])
            if check:
                attrs['otp_check'] = check
            else:
                raise ValidationError('OTP incorrect or OTP lifetime pass, please')
        else:
            attrs['sms_otp'] = send_sms_code(attrs['phone'], 'Verify code: ')

        return attrs

    def login_user(self, request, user):
        if self.validated_data['otp_check']:
            login(request, user)
            return True
        else:
            return False

    def check_token(self, token):
        pass