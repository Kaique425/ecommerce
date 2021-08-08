from django.urls import path
from . import views
APP_NAME="product"
urlpatterns = [
    path("", views.ProductListView.as_view(), name="list"),
    path("product/<int:id>", views.ProductsDetailView.as_view(), name="detail")
]