from django.urls import path
from . import views


app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pk>/update_task/', views.update, name='update'),
    path('<str:pk>/detele/', views.delete, name='delete')
]
