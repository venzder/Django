import json
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from django.http import Http404, JsonResponse
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from products.models import Category
from products.forms import CategoryForm, CategoryModelForm


class RestCategoryListView(ListView):
    model = Category

    def serialize_object_list(self, queryset):
        return list(
            map(
                lambda itm: {
                    'id': itm.id,
                    'name': itm.name,
                },
                queryset
            )
        )

    def get_context_data(self, **kwargs):
        context = super(RestCategoryListView, self).get_context_data(**kwargs)
        object_list = context.get('object_list')

        data = {}
        data['results'] = self.serialize_object_list(object_list)
        return data

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class CategoryListView(ListView):
    model = Category
    template_name = 'categories/catalog.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/detail.html'

    # def get_context_data(self, **kwargs):
    #     key = self.context_object_name if self.context_object_name else 'object'
    #     obj = kwargs.get(key)
    #     products = obj.product_set.all()
    #     page = self.request.GET.get('page')
    #     paginator = Paginator(products, 2)
    #     page_obj = paginator.get_page(page)
    #     return {
    #         key: obj,
    #         'products': page_obj
    #     }


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryModelForm
    template_name = 'categories/create.html'
    success_url = reverse_lazy('categories:list')


class CategoriesUpdateView(UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'categories/update.html'
    success_url = reverse_lazy('categories:list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories/delete.html'
    success_url = reverse_lazy('categories:list')


def category_create_view(request):
    form = CategoryModelForm()
    success_url = reverse('products:list')
    if request.method == 'POST':
        form = CategoryModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            # obj = Category(
            #     name=form.cleaned_data.get('name'),
            #     description=form.cleaned_data.get('description')
            # )
            # obj.save()
            return redirect(success_url)
    return render(
        request,
        'categories/create.html',
        {'form': form}
    )


def category_update_view(request, pk):
    try:
        obj = Category.objects.get(pk=pk)
    except Exception as arr:
        raise Http404
    form = CategoryModelForm(instance=obj)
    success_url = reverse('products:list')
    if request.method == 'POST':
        form = CategoryModelForm(
            request.POST,
            files=request.FILES,
            initial=obj
        )
        if form.is_valid():
            form.save()
            return redirect(success_url)
    return render(
        request,
        'categories/update.html',
        {'form': form}
    )

