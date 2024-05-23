
from django.urls import path
from .views import index, sinoplu_list, sinoplu_add, sinoplu_update, sinoplu_detail, sinoplu_delete, filter_list


urlpatterns = [ 
    path('', index, name="index"),
    path('list/', sinoplu_list, name='list' ),
    path('add/', sinoplu_add, name='add'),
    path('update/<int:id>', sinoplu_update, name='update'),
    path('delete/<int:id>', sinoplu_delete, name='delete'),
    path('sinoplu/<int:id>', sinoplu_detail, name="detail"),
    path('filter_list', filter_list, name="filter"),
]
