from django.urls import path
from webapp import views as page


urlpatterns = [
    path('', page.home_page, name='index-page'),
    path('products', page.product_all_page, name='product-all-page'),
    path('products/add', page.product_add_page, name='product-add-page'),
    path('products/category', page.product_category_page, name='product-category-page'),
    path('products/type', page.product_type_page, name='product-type-page'),
]
