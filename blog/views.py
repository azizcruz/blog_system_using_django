from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

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
            messages.success(request, 'Post Added.')
            return HttpResponseRedirect(instance.get_post_url())
    else:
        form = PostForm()
        context = {
            'form': form,
            'title': 'Add Post'
        }

    return render(request, 'blog/form.html', context)

def edit_post(request, id):
    instance = get_object_or_404(Post, id=id)
    if request.POST:
        form = PostForm(request.POST, request.FILES, instance=instance)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Post edited')
            return HttpResponseRedirect(instance.get_post_url())

    else:
        form = PostForm(instance=instance)
        context = {
            'form': form,
            'title': 'Edit Post'
        }

    return render(request, 'blog/form.html', context)

def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.warning(request, 'Post deleted.')
    return redirect('main')
