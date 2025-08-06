from rest_framework import serializers
from .models import Recipe, Ingredient, Step, Review, Notification, SavedRecipe

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['id', 'order', 'description']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'comment', 'rating', 'created_at']

class RecipeListSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'author', 'time', 'image', 'rating']

    def get_rating(self, obj):
        avg = obj.average_rating()
        return f"{avg:.1f}" if avg is not None else "0.0"

class FullRecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    steps = StepSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = '__all__'

    def get_rating(self, obj):
        avg = obj.average_rating()
        return f"{avg:.1f}" if avg is not None else "0.0"

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'title', 'body', 'type', 'is_read', 'created_at']

class SavedRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedRecipe
        fields = ['id', 'recipe', 'device_id', 'saved_at']
