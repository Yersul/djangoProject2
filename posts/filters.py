import django_filters
from django.db.models import Q
from django_filters import rest_framework as filters



# class ProductFilterSet(filters.FilterSet):
#     name = filters.CharFilter(field_name='name', lookup_expr='contains')
#     cost = filters.NumberFilter(field_name='cost', lookup_expr='gt')
#
#     class Meta:
#         model = Product
#         fields = ('name', 'description', 'cost', 'owner')
from posts.models import Blog


class BlogFilterSet(filters.FilterSet):
    search = filters.CharFilter(method='filter_by_value', label='Search')
    search2 = filters.CharFilter(field_name='search2')

    class Meta:
        model = Blog
        fields = ('search', )

    def filter_by_value(self, queryset, title, text):
        filter_params = Q()
        if self.request.query_params['search']:
            list_of_words = list(map(str, self.request.query_params['search'].split()))
            for word in list_of_words:
                filter_params |= Q(title__contains=word)
                filter_params |= Q(text__contains=word)
        result = queryset.filter(filter_params)
        return result
