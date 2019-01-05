from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm, SingUpForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

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
        'page_var': page_var,
        'current_user': request.user
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
    instance = get_object_or_404(Post, id=id)

    if instance.user == request.user or request.user.is_superuser:
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
    else:
        return redirect('main')


def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    if post.user == request.user or request.user.is_superuser:
        post.delete()
        messages.warning(request, 'Post deleted.')
        return redirect('main')

def signup(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.save()
            messages.success(request, 'Your account was created successfully.')
            return redirect('main')
    else:
        form = SingUpForm()

    context = {
       'title': 'Sign up',
       'form': form
   }
    return render(request, 'registration/signup.html', context)
