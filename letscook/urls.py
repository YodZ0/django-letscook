from django.urls import path
from .views import index, cabinet_view, catalog_view, recipe_detail_view, add_recipe_view, delete_recipe

urlpatterns = [
    path('', index, name='index'),
    path('cabinet/', cabinet_view, name='cabinet'),
    path('cabinet/add-recipe/', add_recipe_view, name='add-recipe'),
    path('cabinet/delete-recipe/<slug:slug>', delete_recipe),
    path('detail/<slug:slug>', recipe_detail_view, name='detail'),
    path('catalog/', catalog_view, name='catalog'),
]
