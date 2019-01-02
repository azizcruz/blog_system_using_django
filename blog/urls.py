from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='main'),
    path(r'post/create/', views.create_post, name='create_post'),
    path(r'post/<int:id>/edit', views.edit_post, name='edit_post'),
    path(r'detail/<int:id>/', views.post_detail, name='post_detail'),
    path(r'post/<int:id>/delete', views.delete_post, name='delete_post')
]
