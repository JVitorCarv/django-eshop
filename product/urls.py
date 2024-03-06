from django.urls import path
from . import views

urlpatterns = [
    path("products/", view=views.get_products, name="products"),
    path("products/<str:pk>", view=views.get_product, name="get_product_details"),
]
