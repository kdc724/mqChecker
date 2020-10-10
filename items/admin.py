from django.contrib import admin
from . models import Category, Condition, Team, Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'category', 'status', 'team', 'condition','priority','date_checked')
  list_display_links = ('id', 'title')
  list_filter = ('category','status', 'team', 'condition',)
  search_fields = ('title', 'category', 'status', 'team', 'condition','priority','date_checked')
  list_per_page = 25




admin.site.register(Category)
admin.site.register(Condition)
admin.site.register(Team)
admin.site.register(Item,ItemAdmin)

