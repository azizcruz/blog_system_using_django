from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def index(request):
    query = Post.objects.all().order_by('-publish_date')
    q = request.GET.get('q')

    # Search field functionality
    if q:
        query = query.filter(
            Q(title__icontains = q) | Q(content__icontains = q)
            )

    paginator = Paginator(query, 2) # Show 1 post per page
    page = request.GET.get('page') # Get number of the page from the link
    posts_pages = paginator.get_page(page) # Request the number of the page to show
    page_var = 'page'

    context = {
        'title': 'Main',
        'posts_pages': posts_pages,
        'page_var': page_var
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
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    if request.POST:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user
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
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

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
