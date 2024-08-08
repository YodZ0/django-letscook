from django.contrib import admin
from .models import RecipeModel, IngredientModel, TagModel, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(RecipeModel)
class RecipeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_tags', 'user', 'create_date']
    list_display_links = ['id', 'title']

    readonly_fields = ['user', 'create_date']
    fields = ('title', 'slug', 'description', 'steps', 'tags', 'video_url', 'create_date', 'user')
    filter_horizontal = ['tags']

    inlines = (RecipeIngredientInline,)

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    @admin.display(description='Tags')
    def get_tags(self, obj):
        return ', '.join(obj.tags_list)


@admin.register(IngredientModel)
class IngredientModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit', 'group']
    inlines = (RecipeIngredientInline,)
    save_on_top = True
    list_filter = ('group',)


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    ordering = ['order']
