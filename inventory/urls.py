from django.urls import path
from .views import DeleteUserView
from .views import (
    ProductListView, ProductCreateView, ProductDetailView,
    ProductUpdateView, ProductDeleteView
)

urlpatterns = [
    path('list/', ProductListView.as_view()),
    path('create/', ProductCreateView.as_view()),
    path('read/<uuid:product_id>/', ProductDetailView.as_view()),
    path('update/<uuid:product_id>/', ProductUpdateView.as_view()),
    path('delete/<uuid:product_id>/', ProductDeleteView.as_view()),
    path('delete_user/<int:user_id>/', DeleteUserView.as_view()),
]
