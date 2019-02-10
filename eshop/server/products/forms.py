from django import forms
from .models import Category


class CategoryForm(forms.Form):
    name = forms.CharField(required=True)
    description = forms.CharField(widget=forms.widgets.Textarea())

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

