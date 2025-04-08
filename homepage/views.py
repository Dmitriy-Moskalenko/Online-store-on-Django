from django.shortcuts import render

from homepage.forms import SearchForm
from products.models import Products
from products.service import all_products, all_categories


def home_page(request):
    """Главная страница"""
    return render(request, 'home_page.html', {
        'all_products': all_products(),
        'all_categories': all_categories(),
        'search_form': SearchForm(request.GET),
    })


def search(request):
    """Поиск по сайту"""
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            form_data = form.cleaned_data['search']
            result = Products.objects.filter(title__icontains=form_data)
            return render(request, 'result_search.html', {
                'result_search': result
            })
    else:
        form = SearchForm(request.GET)
    return render(request, 'result_search.html', {
        'search_form': form
    })