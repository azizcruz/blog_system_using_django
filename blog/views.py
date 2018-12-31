from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.

def index(request):
    query = Post.objects.all().order_by('-publish_date')
    context = {
        'title': 'Main',
        'posts': query
    }

    return render(request, 'blog/posts.html', context)

def post_detail(request, id):
    pass
