from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

import json

from .services import (create_recipe, all_ingredients, all_tags, all_recipies,
                       get_all_user_recipies, get_recipe_by_slug, get_recipe_ingredients, delete_recipe_obj)


def index(request):
    recipe = get_recipe_by_slug('some-test-recipe-12345')
    context = {'recipe': recipe}
    return render(request, template_name='letscook/index.html', context=context)


def catalog_view(request):
    recipies = all_recipies(prefetch_related=('tags',),
                            only=('title', 'slug', 'description', 'user__username', 'tags__name', 'create_date'),
                            order_by=('-id', '-create_date'))

    paginator = Paginator(recipies, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'pages': page_obj}
    return render(request=request, template_name='letscook/catalog-page.html', context=context)


def cabinet_view(request):
    if not request.user.is_authenticated:
        messages.info(request=request, message='You have to log in!')
        return redirect('login')
    else:
        user = request.user
        recipies = get_all_user_recipies(user)
        count = len(recipies)
        context = {
            'user': user,
            'recipies': recipies,
            'count': count,
        }
    return render(request=request, template_name='letscook/cabinet.html', context=context)


def add_recipe_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = request.user
        create_recipe(data, user)

        response = {'redirect_url': '/cabinet/'}
        messages.success(request=request, message='Recipe has been added!')
        return JsonResponse(data=response, status=200)
    else:
        ingredients = all_ingredients()
        tags = all_tags(order_by=('order',))
        context = {
            'ingredients': ingredients,
            'tags': tags,
        }
    return render(request=request, template_name='letscook/add-recipe.html', context=context)


def recipe_detail_view(request, slug):
    recipe = get_recipe_by_slug(slug)
    ingredients = get_recipe_ingredients(recipe)
    recipe_steps = json.loads(recipe.steps)

    is_author = False
    if request.user == recipe.user:
        is_author = True

    context = {
        'title': recipe.title,
        'description': recipe.description,
        'recipe_steps': recipe_steps,
        'user': recipe.user,
        'tags': recipe.tags.all,
        'video': recipe.video_url,
        'create_date': recipe.create_date,
        'ingredients': ingredients,
        'is_author': is_author,
        'slug': recipe.slug,
    }
    return render(request=request, template_name='letscook/recipe-detail.html', context=context)


def delete_recipe(request, slug):
    if request.method == 'POST':
        recipe = get_recipe_by_slug(slug)
        delete_recipe_obj(recipe)

        response = {'redirect_url': '/cabinet/'}
        messages.error(request=request, message='Recipe has been deleted!')
        return JsonResponse(data=response, status=200)
    else:
        return redirect(to='cabinet')
