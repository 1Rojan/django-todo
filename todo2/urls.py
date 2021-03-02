from django.urls import path
from . import views

app_name = 'todo2'
urlpatterns= [
    path('', views.index_template),
    path('edit/<int:pk>', views.edit_template, name='edit_template'),
    path('delete/<int:pk>', views.delete_template, name='delete_template')
]