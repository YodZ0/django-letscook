from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .services import get_user_cart, get_cart_recipies, add_recipe_to_cart, delete_recipe_from_cart


def cart_view(request):
    if not request.user.is_authenticated:
        messages.info(request=request, message='You have to log in!')
        return redirect('login')
    else:
        user = request.user
        cart = get_user_cart(user)
        cart_recipies, total_ingredients = get_cart_recipies(cart)
        count = len(cart_recipies)

        context = {
            'cart': cart,
            'cart_recipies': cart_recipies,
            'count': count,
            'total_ingredients': sorted(total_ingredients.items()),
        }
        return render(request=request, template_name='cart/cart.html', context=context)


def add_recipe_to_cart_view(request, slug):
    if request.method == 'POST':
        user = request.user
        add_recipe_to_cart(slug, user)
        response = {'ok': 'ok'}
        return JsonResponse(data=response, status=200)
    else:
        return redirect(to='catalog')


def delete_recipe_from_cart_view(request, slug):
    if request.method == 'POST':
        user = request.user
        delete_recipe_from_cart(slug, user)
        response = {'ok': 'ok'}
        return JsonResponse(data=response, status=200)
    else:
        return redirect(to='catalog')
