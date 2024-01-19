from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('delete/<int:delid>', views.delete,name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('home1', views.taskListView.as_view(), name='home1'),
    path('detail1/<int:pk>', views.taskDetailView.as_view(), name='detail1'),
    path('update1/<int:pk>', views.taskUpdateView.as_view(), name='update1'),
    path('delete1/<int:pk>', views.taskDeleteView.as_view(), name='delete1'),
]