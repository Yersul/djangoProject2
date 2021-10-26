from django.http import Http404
from rest_framework import viewsets, mixins, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters import rest_framework as filters

from comment.models import Comment
from comment.permissions import CommentOwnerOrReadOnly
from comment.serializers import CommentSerializer, CommentCreateSerializer, CommentUpdateSerializer


class CommentViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet,):
    queryset = Comment.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = CommentSerializer

    def get_permissions(self):
        permission_classes = [AllowAny, ]

        if self.action == 'retrieve' or self.action == 'create':
            permission_classes = [IsAuthenticated, CommentOwnerOrReadOnly]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes.append(CommentOwnerOrReadOnly)

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        serializer_class = CommentSerializer

        if self.action == 'create':
            serializer_class = CommentCreateSerializer
        elif self.action == 'update':
            serializer_class = CommentUpdateSerializer
        return serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer_data = CommentSerializer(instance).data
        return Response(data=serializer_data, status=status.HTTP_201_CREATED)

    # def list(self, request, *args, **kwargs):
    #     filtered_queryset = self.filter_queryset(self.queryset.all())
    #     serializer = self.get_serializer(filtered_queryset, many=True)
    #     return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
