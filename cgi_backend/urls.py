from django.urls import path

from . import views

urlpatterns = [
    path('getData/', views.index, name='getData'),
    path('getData/<key>/<v>/', views.filter_data, name='getData'),
    path('getView/', views.get_view, name='getView'),
    path('insert/', views.insert, name='insert')
]