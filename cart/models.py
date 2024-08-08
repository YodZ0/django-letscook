from django.contrib.auth.models import User
from django.db import models

from letscook.models import RecipeModel


class UserCart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    recipies = models.ManyToManyField(to=RecipeModel, null=True, blank=True)

    def __str__(self):
        return f'{self.user} Cart'
