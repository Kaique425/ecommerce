from django.urls import path
from django.urls.conf import include
from . import views
app_name="product"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="list"),
    path("product/<slug:slug>", views.ProductsDetailView.as_view(), name="detail")
]