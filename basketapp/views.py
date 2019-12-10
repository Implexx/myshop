from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product


# Create your views here.


def basket_view(request):
    context_list = {}
    return render(request, 'basket.html', context_list)


def basket_add_view(request, pk):
    product = get_object_or_404(Product, pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove_view(request, pk):
    context_list = {}
    return render(request, 'basket.html', context_list)
