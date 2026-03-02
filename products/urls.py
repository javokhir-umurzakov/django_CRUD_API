from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ProductViewSet, product_page, login_view, delete_product

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = router.urls + [
    path('login/', login_view, name='login'),
    path('products-page/', product_page, name='product_page'),
    path('products/delete/<int:id>/', delete_product, name='delete_product'),
]