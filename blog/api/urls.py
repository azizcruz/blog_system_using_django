from django.urls import path
from .views import (PostsAPIList, SinglePostAPI, EditePostAPI, AddPostAPI, DeletePostAPI)

urlpatterns = [
    path(r'', PostsAPIList.as_view(), name='list_posts'),
    path(r'add/', AddPostAPI.as_view(), name='add'),
    path(r'<pk>/', SinglePostAPI.as_view(), name='single_post'),
    path(r'<pk>/edit/', EditePostAPI.as_view(), name='edit'),
    path(r'<id>/delete/', DeletePostAPI.as_view(), name='delete')
]
