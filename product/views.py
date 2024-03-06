from .filters import ProductsFilter
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from eshop.utils.filter import get_filter_parameters


# Create your views here.
@swagger_auto_schema(
    method="get",
    manual_parameters=get_filter_parameters(ProductsFilter),
    responses={200: ProductSerializer(many=True)},
)
@api_view(["GET"])
def get_products(request):
    filterset = ProductsFilter(
        request.GET, queryset=Product.objects.all().order_by("id")
    )
    serializer = ProductSerializer(filterset.qs, many=True)
    return Response({"data": serializer.data})


@swagger_auto_schema(
    method="get",
    responses={200: ProductSerializer()},
)
@api_view(["GET"])
def get_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response({"data": serializer.data})
