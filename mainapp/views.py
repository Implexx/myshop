import random
from django.shortcuts import render
from .models import Team, Review, BrandLogo, Product, ProductCategory
from basketapp.models import Basket
from django.shortcuts import get_object_or_404


# Create your views here.


def main_view(request):
    context_list = {"name": 'Maksim'}
    return render(request, 'mainapp/index.html', context_list)


def about_view(request):
    title = 'О команде'
    all_team = Team.objects.all()[:4]
    img_alt = 'teammate_photo'
    context_list = {'title': title, 'all_team': all_team, 'img_alt': img_alt}
    return render(request, 'about.html', context_list)


def account_view(request):
    context_list = {}
    return render(request, 'account.html', context_list)


def cart_view(request):
    context_list = {}
    return render(request, 'cart.html', context_list)


def checkout_view(request):
    context_list = {}
    return render(request, 'checkout.html', context_list)


def contact_view(request):
    context_list = {'title': 'Контакты'}
    return render(request, 'contact.html', context_list)


def my_account_view(request):
    context_list = {}
    return render(request, 'my-account.html', context_list)


def product_details_view(request, pk=None):
    """
    Страница детальной информации продукта
    TODO: разобраться как выбирать нужную картинку из списка, пока выводится только первая
    :param request:
    :param pk:
    :return:
    """
    print('pk=', pk)

    title = 'Детальная информация'
    links_menu = ProductCategory.objects.all()
    all_reviews = Review.objects.all()
    basket = get_basket(request.user)

    # если есть первичный ключ товара
    if pk is not None:
        print('pk > 1')
        product = get_object_or_404(Product, pk=pk)
        related_products = get_same_category_products(product)
        print('product=', product)
        print('related_products=', related_products)
    else:
        # если нет никакого первичного ключа товара то горячий продукт. Пока рандомный просто
        product = get_random_hot_product()
        related_products = get_same_category_products(product)

    context_list = {'title': title,
                    'all_reviews': all_reviews,
                    'links_menu': links_menu,
                    'basket': basket,
                    'product': product,
                    'related_products': related_products,
                    }
    return render(request, 'product-details.html', context_list)


def products_view(request, pk=None):
    """
    Контроллер списка товаров по категориям
    TODO: разобраться как выбирать нужную картинку из списка, пока выводится только первая
    :param request:
    :param pk:
    :return:
    """
    print('pk=', pk)

    title = 'Продукты'
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    # если есть первичный ключ

    if pk is not None:
        print('pk <> 0')
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
            print('products=', products)

        context_list = {'title': title,
                        'links_menu': links_menu,
                        'category': category,
                        'products': products,
                        'basket': basket
                        }
        return render(request, 'products_list.html', context_list)

    # если нет никакого первичного ключа
    same_products = Product.objects.all()[0:8]
    context_list = {'title': title,
                    'links_menu': links_menu,
                    'same_products': same_products,
                    'basket': basket,
                    }
    return render(request, 'products.html', context_list)


def shop_view(request):
    context_list = {}
    return render(request, 'mainapp/products.html', context_list)


def shop_list_view(request):
    context_list = {}
    return render(request, 'mainapp/products_list.html', context_list)


def wishlist_view(request):
    context_list = {}
    return render(request, 'wishlist.html', context_list)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_random_hot_product():
    products = Product.objects.filter(is_hot=True)

    return random.sample(list(products), 1)[0]


def get_same_category_products(some_product):
    same_products = Product.objects.filter(category=some_product.category).exclude(pk=some_product.pk)[:3]
    return same_products


