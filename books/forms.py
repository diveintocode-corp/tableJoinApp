from django import forms


class BookForm(forms.Form):
    title = forms.CharField(label='Title', max_length=255)
    user = forms.IntegerField(label='User')
