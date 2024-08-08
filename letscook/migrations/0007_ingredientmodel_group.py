# Generated by Django 5.0.4 on 2024-06-30 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letscook', '0006_recipemodel_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientmodel',
            name='group',
            field=models.CharField(blank=True, choices=[('meat', 'meat'), ('vegetables', 'vegetables'), ('spices', 'spices'), ('liquid', 'liquid'), ('fruits', 'fruits'), ('greenery', 'greenery'), ('all', 'all')], max_length=50, null=True),
        ),
    ]