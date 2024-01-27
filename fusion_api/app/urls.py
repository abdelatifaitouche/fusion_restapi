from django.urls import path, include
from .views import * 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', getRoutes , name="routes"),
    path('products/' , getProducts , name='product-list'),
    path('product_details/<str:pk>' , getProductDetails, name = 'product-details'),
    path('create_product/' , createProduct , name='addProduct'),

    path('purchase/' , addCommande , name='purchase')
]

urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)