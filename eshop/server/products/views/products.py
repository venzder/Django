import json
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from django.http import JsonResponse
from products.models import Product
from products.forms import ProductModelForm
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)


class RestProductListView(ListView):
    model = Product
    template_name = 'products/catalog.html'
    paginate_by = 2


    def serialize_object_list(self, queryset):
        return list(
            map(
                lambda itm: {
                    'id': itm.id,
                    'name': itm.name,
                    'description': itm.description,
                    'full_description': itm.full_description,
                    'image': itm.image.url if itm.image else None,
                    'category': itm.category.name if itm.category else None,
                    'alt': itm.alt,
                    'title': itm.title,
                    'coast': itm.coast,
                },
                queryset
            )
        )

    def get_context_data(self, **kwargs):
        context = super(RestProductListView, self).get_context_data(**kwargs)
        data = {}
        page = context.get('page_obj')
        route_url = reverse('rest_products:list')
        data['next_url'] = None
        data['previous_url'] = None
        data['page'] = page.number
        data['count'] = page.paginator.count
        data['results'] = self.serialize_object_list(page.object_list)

        if page.has_previous():
            data['previous_url'] = f'{route_url}?page={page.previous_page_number()}'
        if page.has_next():
            data['next_url'] = f'{route_url}?page={page.next_page_number()}'
        return data

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class ProductListView(ListView):
    model = Product
    template_name = 'products/catalog.html'
    paginate_by = 2
    # def get_context_data(self, **kwargs):
    #     context = super(ProductListView, self).get_context_data(**kwargs)
    #     queryset = context.get('object_list')
    #     page = self.request.GET.get('page')
    #     paginator = Paginator(queryset, 5)
    #     page_obj = paginator.get_page(page)
    #     context['page_obj'] = page_obj
    #     return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductModelForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = [
        'name', 'description', 'full_description', 'image', 'category', 'alt', 'title', 'coast'
    ]
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:list')


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


def product_create_view(request):
    form = ProductModelForm()
    success_url = reverse('products:list')
    if request.method == 'POST':
        form = ProductModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    return render(
        request,
        'products/create.html',
        {'form': form}
    )


def product_update_view(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    form = ProductModelForm(instance=obj)
    success_url = reverse('products:list')
    if request.method == 'POST':
        form = ProductModelForm(
            request.POST,
            files=request.FILES,
            instance=obj
        )
        if form.is_valid():
            form.save()
            return redirect(success_url)
    return render(
        request,
        'products/update.html',
        {'form': form}
    )


def product_delete_view(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    success_url = reverse('products:list')
    if request.method == 'POST':
        obj.delete()
        return redirect(success_url)

    return render(
        request,
        'products/delete.html',
        {'object': obj}
    )