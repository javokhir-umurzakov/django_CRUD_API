from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from drf_yasg.utils import swagger_auto_schema

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Get all products")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create new product")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


def product_page(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def delete_product(request, id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=id)
        product.delete()
    return redirect('product_page')



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('product_page')
        else:
            return render(request, 'products/login.html', {'error': 'Invalid credentials'})

    return render(request, 'products/login.html')