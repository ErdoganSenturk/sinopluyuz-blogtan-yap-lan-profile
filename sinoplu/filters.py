import django_filters
from .models import Sinopluyuz


class SinopluFilter(django_filters.FilterSet):
    class Meta:
        model = Sinopluyuz
        fields = {
            'first_name' : ['icontains'],
            'last_name' : ['icontains'],
            'sehir' : ['exact'],
            'kategori' : ['exact']
        }

#  ['first_name', 'last_name']