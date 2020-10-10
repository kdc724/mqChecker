import django_filters
from django_filters import DateFilter, CharFilter
from django_filters.widgets import RangeWidget

from .models import Item

class ItemFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_checked", lookup_expr='gt',label='From:')
	end_date = DateFilter(field_name="date_checked", lookup_expr='lt',label='To:')
	note = CharFilter(field_name='comments', lookup_expr='icontains')
	title_contains = CharFilter(field_name='title', lookup_expr='icontains')
	date_checked = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'type': 'date'}))


	class Meta:
		model = Item
		fields = '__all__'
		exclude = ['date_created','photo_main']