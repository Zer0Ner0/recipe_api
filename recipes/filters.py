import django_filters
from .models import Recipe

class RecipeFilter(django_filters.FilterSet):
    min_rating = django_filters.NumberFilter(method='filter_min_rating')

    class Meta:
        model = Recipe
        fields = []

    def filter_min_rating(self, queryset, name, value):
        filtered = [r.id for r in queryset if (r.average_rating() or 0) >= value]
        return queryset.filter(id__in=filtered)
