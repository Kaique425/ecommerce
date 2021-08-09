from django.urls import path
from . import views
app_name="product"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="list"),
    path("product/<int:pk>", views.ProductsDetailView.as_view(), name="detail")
]