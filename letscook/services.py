from .models import RecipeModel, TagModel, IngredientModel, RecipeIngredient

import json

from common.common_services import all_objects, filter_objects, get_object, delete_object, create_object


def create_recipe(data, user):
    recipe_steps = json.dumps(_clear_steps_elements(data['steps']))
    ingredients = data['ingredients']
    recipe_tags = filter_objects(objects=TagModel.objects, name__in=data['tags'])
    video_link = (_parse_video_url(data['video_url']) if data['video_url'] else '')

    recipe_obj = create_object(objects=RecipeModel.objects,
                               title=data['title'],
                               description=data['description'],
                               user=user,
                               steps=recipe_steps,
                               video_url=video_link,
                               )
    _set_tags(recipe_obj, recipe_tags)
    _add_ingredients_to_recipe(recipe_obj=recipe_obj, ingredients_dict=ingredients)


def _set_tags(obj, tags):
    obj.tags.add(*tags)


def _clear_steps_elements(recipe_steps: list[str]) -> list[str]:
    clear_steps = [step.strip() for step in recipe_steps if step]
    return clear_steps


def _parse_video_url(url: str) -> str:
    video_code = url.split('https://www.youtube.com/')[1].split('watch?v=')[1]
    video_link = 'https://www.youtube.com/embed/' + video_code
    return video_link


def _add_ingredients_to_recipe(recipe_obj: RecipeModel, ingredients_dict: dict[str, str]) -> None:
    ingredients_names_list = [name for name in ingredients_dict.keys()]
    ingredients = filter_objects(objects=IngredientModel.objects, name__in=ingredients_names_list)
    for ingredient in ingredients:
        count = float(ingredients_dict[ingredient.name])
        create_object(objects=RecipeIngredient.objects, recipe=recipe_obj, ingredient=ingredient, count=count)


def all_ingredients(**kwargs):
    return all_objects(objects=IngredientModel.objects, **kwargs)


def all_tags(**kwargs):
    return all_objects(objects=TagModel.objects, **kwargs)


def all_recipies(**kwargs):
    return all_objects(objects=RecipeModel.objects, **kwargs)


def get_all_user_recipies(user):
    return filter_objects(objects=RecipeModel.objects,
                          user=user,
                          order_by=('-id', '-create_date',))


def get_recipe_by_slug(slug):
    return get_object(objects=RecipeModel.objects, slug=slug)


def get_recipe_ingredients(recipe_obj):
    return filter_objects(objects=RecipeIngredient.objects, recipe=recipe_obj)


def delete_recipe_obj(recipe_obj):
    return delete_object(recipe_obj)
