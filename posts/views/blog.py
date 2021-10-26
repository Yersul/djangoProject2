from django.http import Http404
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters import rest_framework as filters
from django.views.generic import UpdateView

from posts.filters import BlogFilterSet
from posts.models import Blog
from posts.serializers import BlogSerializer, BlogCreateSerializer, BlogDeleteSerializer, BlogModerateSerializer
from posts.permissions import PostOwnerOrReadOnly, PostStaffEditOnly


class BlogViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet,):
    permission_classes = [AllowAny, ]
    serializer_class = BlogSerializer
    queryset = Blog.objects.filter(is_moderated=True)

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BlogFilterSet

    def get_serializer_class(self):
        serializer_class = BlogSerializer

        if self.action == 'create':
            serializer_class = BlogCreateSerializer
        elif self.action == 'delete':
            serializer_class = BlogDeleteSerializer

        return serializer_class

    def get_permissions(self):
        permission_classes = [AllowAny, ]

        if self.action == 'retrieve' or self.action == 'create':
            permission_classes = [IsAuthenticated, PostOwnerOrReadOnly]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes.append(PostOwnerOrReadOnly)

        return [permission() for permission in permission_classes]

    # def get(self, request, *args, **kwargs):
    #
    #     if 'uuid' in kwargs.keys():
    #         serializer = self.serializer_class(self.queryset.get(pk=kwargs['uuid']))
    #         response = serializer.data
    #         response['comments'] = serializer.add_comment(response['uuid'])
    #     else:
    #         response = self.serializer_class(self.queryset.all(), many=True).data
    #
    #     return Response(data=response, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer_data = BlogCreateSerializer(instance).data
        return Response(data=serializer_data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        filtered_queryset = self.filter_queryset(self.queryset.all())
        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response(serializer.data)

    def get_blogs(self):
        owner = self.request.user

        try:
            instance = Blog.objects.filter(owner=owner)
            return instance
        except:
            raise Http404

    def get_object(self):
        uuid = self.kwargs['pk']
        try:
            instance = self.queryset.get(uuid=uuid)
            return instance
        except:
            raise Http404


class UpdatePostView(UpdateView):
    model = Blog
    fields = ['title', 'text']


class BlogModerateViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet,):
    permission_classes = [IsAuthenticated, ]
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BlogFilterSet

    def get_serializer_class(self):
        serializer_class = BlogSerializer
        if self.action == 'update':
            serializer_class = BlogModerateSerializer
        return serializer_class

    def get_permissions(self):
        permission_classes = [IsAuthenticated, ]

        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated, PostStaffEditOnly]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes.append(PostStaffEditOnly)

        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
