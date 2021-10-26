from django_filters import DateRangeFilter, DateFilter
import django_filters
from likes.models import Like


class LikesFilterSet(django_filters.FilterSet):
    start = django_filters.DateFilter(field_name='created_at',lookup_expr='lt',label='Date liked is before (mm/dd/yyyy):')
    end = django_filters.DateFilter(field_name='created_at',lookup_expr='gt',label='Date liked is after (mm/dd/yyyy):')
    created_at = DateRangeFilter()

    class Meta:
        model = Like
        fields = ['created_at']