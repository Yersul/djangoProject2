from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import logout

from users.models import CustomUser
from users.serializers.logout import LogoutSerializer


class BlacklistRefreshView(APIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = LogoutSerializer
    queryset = CustomUser.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        logout(request)
        return Response("Success", status=status.HTTP_401_UNAUTHORIZED)
