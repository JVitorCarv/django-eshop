from .filters import ProductsFilter
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from utils.swagger.filter import get_filter_parameters
from utils.swagger.pagination import get_pagination_parameters
from utils.type_parsers import parse_posint
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


# Create your views here.
@swagger_auto_schema(
    method="get",
    manual_parameters=[
        *get_pagination_parameters(),
        *get_filter_parameters(ProductsFilter),
    ],
    responses={200: ProductSerializer(many=True)},
)
@api_view(["GET"])
def get_products(request):
    filterset = ProductsFilter(
        request.GET, queryset=Product.objects.all().order_by("id")
    )
    count = filterset.qs.count()

    res_per_page = parse_posint(request.GET.get("res_per_page", 1))

    paginator = PageNumberPagination()
    paginator.page_size = res_per_page
    queryset = paginator.paginate_queryset(filterset.qs, request)
    serializer = ProductSerializer(queryset, many=True)
    return Response(
        {"count": count, "res_per_page": res_per_page, "data": serializer.data}
    )


@swagger_auto_schema(
    method="get",
    responses={200: ProductSerializer()},
)
@api_view(["GET"])
def get_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response({"data": serializer.data})
