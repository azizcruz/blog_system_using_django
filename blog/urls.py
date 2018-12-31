from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='main'),
    path(r'^detail/', views.post_detail, name='post_detail')
]
