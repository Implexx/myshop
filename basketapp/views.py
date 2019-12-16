from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


# Create your views here.


def basket_view(request):
    title = 'Корзина'
    links_menu = ProductCategory.objects.all()
    basket_items = Basket.objects.filter(user=request.user).order_by('product__category')
    context_list = {'title': title,
                    'links_menu': links_menu,
                    'basket_items': basket_items
                    }
    return render(request, 'basket.html', context_list)


def basket_add_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    print('product added')
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove_view(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
