from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request):
    query = Post.objects.all().order_by('-publish_date')
    context = {
        'title': 'Main',
        'posts': query
    }

    return render(request, 'blog/posts.html', context)

def post_detail(request, id):
    query = get_object_or_404(Post, id=id)
    date = query.publish_date.strftime('%A, %D')
    context = {
        'post': query,
        'publish_date': date,
        'title': query.title
    }
    return render(request, 'blog/post_detail.html', context)

def create_post(request):
    if request.POST:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.save()
            form = PostForm()
            context = {
                'success': 'Added successfully.',
                'form': form
            }
    else:
        form = PostForm()
        context = {
            'form': form,
            'title': 'Create Post'
        }

    return render(request, 'blog/form.html', context)
