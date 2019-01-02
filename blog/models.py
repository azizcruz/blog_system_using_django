from django.db import models
from django.shortcuts import reverse
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=None, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to='post_image', default='post_image/default.png')
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def get_post_url(self):
        return reverse('post_detail', kwargs={'id': self.id})
