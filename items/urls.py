from django.urls import path
from  . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('item/<int:item_id>/', views.detail, name='item-detail'),
    path('item/new', views.check_item, name='item-check'),
    path('item/<int:item_id>/update', views.update_item, name='item-update'),
    path('item/<int:item_id>/delete', views.delete_item, name='item-delete'),
    path('item/search', views.search_item , name='item-search'),
    path('item/my-items', views.my_items , name='my-dashboard'),
    path('item/export-csv', views.exporting_csv , name='export-csv'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)