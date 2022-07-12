from django.shortcuts import render
from django.shortcuts import redirect
from .models import Variation
from books.models import Book
from .forms import VariationForm


def index(request):
    variations = Variation.objects.all()
    params = {
        'variations': variations,
    }
    return render(request, 'variations/index.html', params)


def create(request):
    if (request.method == 'POST'):
        kind = request.POST['kind']
        book = Book.objects.get(id=request.POST['book'])
        variation = Variation(kind=kind, book=book)
        variation.save()
        return redirect('variations:index')
    else:
        params = {
            'form': VariationForm(),
        }
        return render(request, 'variations/create.html', params)


def detail(request, variation_id):
    variation = Variation.objects.get(id=variation_id)
    params = {
        'variation': variation,
    }
    return render(request, 'variations/detail.html', params)


def edit(request, variation_id):
    variation = Variation.objects.get(id=variation_id)
    if (request.method == 'POST'):
        variation.kind = request.POST['kind']
        variation.book = Book.objects.get(id=request.POST['book'])
        variation.save()
        return redirect('variations:detail', variation_id)
    else:
        form = VariationForm(initial={
            'kind': variation.kind,
        })
        params = {
            'variation': variation,
            'form': form,
        }
        return render(request, 'variations/edit.html', params)


def delete(request, variation_id):
    variation = Variation.objects.get(id=variation_id)
    if (request.method == 'POST'):
        variation.delete()
        return redirect('variations:index')
    else:
        params = {
            'variation': variation,
        }
        return render(request, 'variations/delete.html', params)
