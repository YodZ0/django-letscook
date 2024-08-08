from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class RecipeModel(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500, unique=True, blank=True)
    description = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, verbose_name='Created by')
    steps = models.TextField()
    tags = models.ManyToManyField(to='TagModel', blank=True)
    ingredients = models.ManyToManyField(to='IngredientModel', through='RecipeIngredient')
    video_url = models.URLField(null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    @property
    def tags_list(self):
        return [tag.name for tag in self.tags.all()]

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'


class IngredientModel(models.Model):
    UNITS = (
        ('unit', 'unit'),
        ('gram', 'g'),
        ('kilogram', 'kg'),
        ('litre', 'l'),
        ('millilitre', 'ml'),
        ('teaspoon', 'teaspoon'),
        ('tablespoon', 'tablespoon'),
    )
    GROUP = (
        ('meat', 'meat'),
        ('fish', 'fish'),
        ('vegetables', 'vegetables'),
        ('spices', 'spices'),
        ('liquid', 'liquid'),
        ('sauce', 'sauce'),
        ('fruits', 'fruits'),
        ('greenery', 'greenery'),
        ('all', 'all'),
    )

    name = models.CharField(max_length=50, unique=True, blank=False)
    unit = models.CharField(max_length=50, choices=UNITS, blank=False)
    group = models.CharField(max_length=50, choices=GROUP, blank=False)

    def __str__(self):
        return f'{self.name}, {self.unit}'

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(to='RecipeModel', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(to='IngredientModel', on_delete=models.CASCADE)
    count = models.FloatField()


class TagModel(models.Model):
    name = models.CharField(max_length=50)
    order = models.IntegerField(default=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
