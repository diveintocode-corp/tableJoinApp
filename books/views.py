from django.shortcuts import render
from django.shortcuts import redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth import get_user_model

User = get_user_model()


def index(request):
    books = Book.objects.all()
    params = {
        'books': books,
    }
    return render(request, 'books/index.html', params)


def create(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        user = User.objects.get(id=request.POST['user'])
        book = Book(title=title, user=user)
        book.save()
        return redirect('books:index')
    else:
        params = {
            'form': BookForm(),
        }
        return render(request, 'books/create.html', params)


def detail(request, book_id):
    book = Book.objects.get(id=book_id)
    params = {
        'book': book,
    }
    return render(request, 'books/detail.html', params)


def edit(request, book_id):
    book = Book.objects.get(id=book_id)
    if (request.method == 'POST'):
        book.title = request.POST['title']
        book.user = User.objects.get(id=request.POST['user'])
        book.save()
        return redirect('books:detail', book_id)
    else:
        form = BookForm(initial={
            'title': book.title,
            'user': book.user.id,
        })
        params = {
            'book': book,
            'form': form,
        }
        return render(request, 'books/edit.html', params)


def delete(request, book_id):
    book = Book.objects.get(id=book_id)
    if (request.method == 'POST'):
        book.delete()
        return redirect('books:index')
    else:
        params = {
            'book': book,
        }
        return render(request, 'books/delete.html', params)
