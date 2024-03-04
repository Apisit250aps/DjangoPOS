from django.shortcuts import render

# Create your views here.


def home_page(request):

    return render(request, 'index/dashboard.html')


def product_all_page(request):

    return render(request, 'products/product-all.html')


def product_add_page(request):

    return render(request, 'products/product-add.html')


def product_category_page(request):

    return render(request, 'products/product-category.html')


def product_type_page(request):
    
    return render(request, 'products/product-type.html')
