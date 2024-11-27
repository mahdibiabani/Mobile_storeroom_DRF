from django_filters.rest_framework import FilterSet
from .models import Mobile

class MobileFilter(FilterSet):
    class Meta:
        model = Mobile
        fields = {
            'brand': ['exact'],
        }