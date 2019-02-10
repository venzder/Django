from django import forms


class CategoryForm(forms.Form):
    name = forms.CharField(required=True)
    description = forms.CharField(widget=forms.widgets.Textarea())
