from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(required=False, label='',
                             widget=forms.TextInput(attrs={'class': 'search-form', 'placeholder': '  Поиск'}))