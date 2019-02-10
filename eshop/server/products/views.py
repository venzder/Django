import json
from django.shortcuts import render
from .models import Product, Category
from .forms import CategoryForm


def product_list_view(request):
    # with open('products/fixtures/data/data.json', encoding='utf-8') as file:
    #     data = json.load(file)
    data = Product.objects.all()
    return render(
        request,
        'products/catalog.html',
        {'object_list': data}
    )


def product_detail_view(request, pk):
    # with open('products/fixtures/data/data.json', encoding='utf-8') as file:
    #     data = json.load(file)
    data = Product.objects.get(pk=pk)
    return render(
        request,
        'products/detail.html',
        {'object': data}
    )


def category_create_view(request):
    form = CategoryForm()
    if request.method == 'POST':
        obj = Category(
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        obj.save()
    return render(
        request,
        'categories/create.html',
        {'form': form}
    )
