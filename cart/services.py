from django.db.models import Prefetch

from letscook.models import RecipeModel, RecipeIngredient
from .models import UserCart

from common.common_services import filter_objects, create_object, get_object
from collections import defaultdict


def get_user_cart(user) -> UserCart:
    cart = filter_objects(objects=UserCart.objects, user=user).prefetch_related(
        Prefetch(
            lookup='recipies',
            queryset=RecipeModel.objects.prefetch_related(
                Prefetch(
                    lookup='recipeingredient_set',
                    queryset=RecipeIngredient.objects.select_related('ingredient')
                )
            )
        )
    ).first()

    if not cart:
        cart = create_object(objects=UserCart.objects, user=user)

    return cart


def get_cart_recipies(cart: UserCart) -> tuple[list, defaultdict]:
    if cart:
        cart_recipies = []
        recipies = cart.recipies.all()
        total_ingredients = defaultdict(float)

        for recipe in recipies:
            ingredients_data = []
            for ri in recipe.recipeingredient_set.all():
                ingredients_data.append({'name': ri.ingredient.name, 'unit': ri.ingredient.unit, 'count': ri.count})
                total_ingredients[f'{ri.ingredient.name}, {ri.ingredient.unit}'] += ri.count

            cart_recipies.append({
                'title': recipe.title,
                'slug': recipe.slug,
                'ingredients': ingredients_data
            })

        return cart_recipies, total_ingredients


def add_recipe_to_cart(slug, user):
    cart = get_object(objects=UserCart.objects, user=user)
    recipe = get_object(objects=RecipeModel.objects, slug=slug)
    cart.recipies.add(recipe)


def delete_recipe_from_cart(slug, user):
    cart = get_object(objects=UserCart.objects, user=user)
    recipe = get_object(objects=RecipeModel.objects, slug=slug)
    cart.recipies.remove(recipe)
