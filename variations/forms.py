from django import forms


class VariationForm(forms.Form):
    kind = forms.CharField(label='Title', max_length=255)
    book = forms.IntegerField(label='Book')
