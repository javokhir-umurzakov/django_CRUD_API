from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = router.urls

from django.urls import path
from .views import product_page,login_view,delete_product

urlpatterns = [
    path('login/', login_view, name='login'),
    path('products/', product_page, name='product_page'),
    path('products/delete/<int:id>/', delete_product, name='delete_product'),
]