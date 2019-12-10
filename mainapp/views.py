from django.shortcuts import render
from .models import Team, Review, BrandLogo, Product, ProductCategory
from django.shortcuts import get_object_or_404


# Create your views here.

CATEGORIES = ProductCategory.objects.all()[0:2]
MORE_CATEGORIES = ProductCategory.objects.all()[2:]


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
    title = 'Детальная информация'
    all_reviews = Review.objects.all()
    related_products = Product.objects.all()[:6]

    product = Product.objects.filter(pk=pk)

    context_list = {'title': title, 'all_reviews': all_reviews,
                    'related_products': related_products, 'product': product}
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
                        'products': products
                        }
        return render(request, 'mainapp/products_list.html', context_list)

    # если нет никакого первичного ключа
    same_products = Product.objects.all()[0:8]
    context_list = {'title': title,
                    'links_menu': links_menu,
                    'same_products': same_products
                    }
    return render(request, 'mainapp/products.html', context_list)


def shop_view(request):
    context_list = {}
    return render(request, 'mainapp/products.html', context_list)


def shop_list_view(request):
    context_list = {}
    return render(request, 'mainapp/products_list.html', context_list)


def wishlist_view(request):
    context_list = {}
    return render(request, 'wishlist.html', context_list)


# def brand_logo_view(request):
#     brands_logo = BrandLogo.objects.all()
#     context_list = {'brands_logo': brands_logo}
#     return render(request, 'includes/inc-brands_subscribes.html', context_list)
