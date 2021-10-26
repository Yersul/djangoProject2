from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from rest_framework import viewsets, mixins, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters import rest_framework as filters

from likes import LikesPutOrReadOnly
from likes.filters import LikesFilterSet
from likes.models import Like
from likes.serializers import LikeSerializer, LikeUpdateSerializer
from posts.models import Blog


class LikesViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet,):
    queryset = Like.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = LikeSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LikesFilterSet

    def get_serializer_class(self):
        serializer_class = LikeSerializer

        if self.action == 'update':
            serializer_class = LikeUpdateSerializer

        return serializer_class

    def get_permissions(self):

        permission_classes = [AllowAny, ]

        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated, LikesPutOrReadOnly]
        elif self.action == 'create' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes.append(LikesPutOrReadOnly)

        return [permission() for permission in permission_classes]

    def post(self, request, *attrs, **kwargs):
        if(len(Like.objects.filter(user = request.user, object_id = request.data['object_id']))>0):
            print('aasd')
            Like.objects.filter(user = request.user, object_id = request.data['object_id']).first().delete()
            return Response({"liked": False}, status=status.HTTP_202_ACCEPTED)
        else:
            try:
                request.data['user'] = request.user.uuid
                request.data['content_type'] = ContentType.objects.get_for_model(Blog).id
                product = Blog.objects.get(uuid = request.data['object_id'])
                contend_data = self.serializer_class(data=request.data, context={'request': request})
                contend_data.is_valid(raise_exception=True)
                contend_data.save()
                return Response({"liked": True}, status=status.HTTP_201_CREATED)
            except:
                return Response({'error': 'no such product uuid'}, status=status.HTTP_404_NOT_FOUND)