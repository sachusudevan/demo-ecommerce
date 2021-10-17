
from django.conf.urls import url
from django.urls import path, include
from . import views
app_name = 'shop'

urlpatterns = [
    path('', views.allProductCat, name="allProductCat"),
    path('<slug:c_slug>/', views.allProductCat, name="products_by_category"),
    path('<slug:c_slug>/<slug:product_slug>',views.prodDetail, name="product_category_detail"),
    
]

