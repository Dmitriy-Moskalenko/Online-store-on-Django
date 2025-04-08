from products.models import Products, Category


def all_products():
    """Все продукты"""
    return Products.objects.all()


def all_categories():
    """Все категории"""
    return Category.objects.all()