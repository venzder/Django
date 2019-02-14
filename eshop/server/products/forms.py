from django import forms
from .models import Category, Product


class CategoryForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'class': 'model-form'}))
    description = forms.CharField(widget=forms.widgets.Textarea(attrs={'class': 'model-form'}))


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'model-form'}),
            'description': forms.widgets.Textarea(attrs={'class': 'model-form'})
        }


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        values = Category.objects.values('id', 'name')
        choices = [(i['id'], i['name']) for i in values]
        fields = ['name', 'description', 'full_description', 'image', 'category', 'alt', 'title', 'coast']
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'model-form'}),
            'description': forms.widgets.TextInput(attrs={'class': 'model-form'}),
            'full_description': forms.widgets.Textarea(attrs={'class': 'model-form'}),
            'image': forms.widgets.FileInput(attrs={'class': 'model-form'}),
            'category': forms.widgets.Select(choices=choices),
            'alt': forms.widgets.TextInput(attrs={'class': 'model-form'}),
            'title': forms.widgets.TextInput(attrs={'class': 'model-form'}),
            'coast': forms.widgets.NumberInput(attrs={'class': 'model-form'})
        }

