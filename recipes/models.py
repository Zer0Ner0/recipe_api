from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    time = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def average_rating(self):
        avg = self.reviews.aggregate(models.Avg('rating'))['rating__avg']
        return round(avg, 1) if avg is not None else None

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=100)

class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='steps')
    step_number = models.IntegerField()
    description = models.TextField()


class RecipeIngredient(models.Model):
    UNIT_CHOICES = [
        ('g', 'grams'),
        ('kg', 'kilograms'),
        ('ml', 'milliliters'),
        ('l', 'liters'),
        ('tsp', 'teaspoon'),
        ('tbsp', 'tablespoon'),
        ('cup', 'cup'),
        ('pcs', 'pieces'),
        ('pinch', 'pinch'),
        ('slice', 'slice'),
    ]

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.FloatField()
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)

    def __str__(self):
        return f"{self.amount} {self.unit} of {self.ingredient.name}"


class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='step_images/', null=True, blank=True)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']


class Review(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not (1 <= self.rating <= 5):
            raise ValidationError("Rating must be between 1 and 5.")

class Notification(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    type = models.CharField(max_length=50, choices=(('like', 'Like'), ('comment', 'Comment')), default='like')

class SavedRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=100)  # simulate user ID for now
    saved_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('recipe', 'device_id')

