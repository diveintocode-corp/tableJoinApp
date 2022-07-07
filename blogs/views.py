from django.shortcuts import render
from django.shortcuts import redirect
from .models import Blog
from .forms import BlogForm


def index(request):
    blogs = Blog.objects.all()
    params = {
        'blogs': blogs,
    }
    return render(request, 'blogs/index.html', params)


def create(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        content = request.POST['content']
        blog = Blog(title=title, content=content)
        blog.save()
        return redirect('blogs:index')
    else:
        params = {
            'form': BlogForm(),
        }
        return render(request, 'blogs/create.html', params)


def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    params = {
        'blog': blog,
    }
    return render(request, 'blogs/detail.html', params)


def edit(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if (request.method == 'POST'):
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.save()
        return redirect('blogs:detail', blog_id)
    else:
        form = BlogForm(initial={
            'title': blog.title,
            'content': blog.content,
        })
        params = {
            'blog': blog,
            'form': form,
        }
        return render(request, 'blogs/edit.html', params)


def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if (request.method == 'POST'):
        blog.delete()
        return redirect('blogs:index')
    else:
        params = {
            'blog': blog,
        }
        return render(request, 'blogs/delete.html', params)
