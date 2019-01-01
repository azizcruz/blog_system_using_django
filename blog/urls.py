from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='main'),
    path(r'post/create/', views.create_post, name='create_post'),
    path(r'detail/<int:id>/', views.post_detail, name='post_detail')
]
