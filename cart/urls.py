from django.urls import path
from .views import cart_view, add_recipe_to_cart_view, delete_recipe_from_cart_view

urlpatterns = [
    path('', cart_view, name='cart'),
    path('add/<slug:slug>', add_recipe_to_cart_view),
    path('delete/<slug:slug>', delete_recipe_from_cart_view),
]
