from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('edit_view/<str:pk>', views.edit_view, name='ediit_view'),
    path('delete_view/<str:pk>', views.delete_view, name='delete_view')
]