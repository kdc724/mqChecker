from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Item

class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = '__all__'
		exclude = ['checker']


class UpdateItemForm(ModelForm):
	class Meta:
		model = Item
		fields = '__all__'
		exclude = ['checker']


#SEARCH FORM TO EXPORT CSV
# class ExportForm(ModelForm):
#	class Meta:
#		model = Item
#		fields = ['title','category','export_csv']