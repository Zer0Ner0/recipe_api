from django.contrib import admin
from django.utils.html import format_html
from .models import Recipe, Ingredient, Step, Review, Notification, SavedRecipe, RecipeIngredient


# === INLINE ===
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1
    fields = ['ingredient', 'amount', 'unit']
    autocomplete_fields = ['ingredient']

class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 1
    fields = ['name', 'image', 'image_preview']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px"/>', obj.image.url)
        return "No Image"

class StepInline(admin.StackedInline):
    model = Step
    extra = 1
    fields = ['order', 'instruction']

class ReviewInline(admin.StackedInline):
    model = Review
    extra = 0
    readonly_fields = ['name', 'comment', 'rating', 'created_at']


# === MAIN FORM ===
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    inlines = [RecipeIngredientInline]
    
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Notification)
admin.site.register(SavedRecipe)