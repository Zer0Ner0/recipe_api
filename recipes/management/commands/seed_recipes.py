import random
from django.core.management.base import BaseCommand
from recipes.models import Recipe, Ingredient, RecipeStep

titles = [
    "Classic Spaghetti Bolognese", "Creamy Chicken Alfredo", "Vegetable Stir Fry",
    "Beef Rendang", "Nasi Lemak", "Tom Yum Soup", "Fish and Chips", "Greek Salad",
    "Chicken Tikka Masala", "Beef Stroganoff", "Pancakes", "Caesar Salad",
    "Butter Chicken", "Fried Rice", "Miso Soup", "Pad Thai", "Shakshuka",
    "Lamb Curry", "Baked Salmon", "Ratatouille", "Pizza Margherita", "Lasagna",
    "Chicken Satay", "Gado-Gado", "Clam Chowder", "Prawn Laksa", "Tandoori Chicken",
    "French Onion Soup", "Moussaka", "Chili Con Carne", "Falafel Wrap", "Quiche Lorraine",
    "Cabbage Soup", "Frittata", "Egg Fried Rice", "Katsu Curry", "Cottage Pie",
    "Biryani", "Sushi Rolls", "Tacos", "Ramen", "Beef Pho", "Tempura Udon",
    "Omelette", "Chicken Fajitas", "Shawarma", "Beef Bulgogi", "Kimchi Stew",
    "Lentil Soup", "Stuffed Peppers"
]

ingredients_list = [
    "Onion", "Garlic", "Tomato", "Olive Oil", "Chicken Breast", "Beef", "Salt", "Pepper",
    "Paprika", "Cumin", "Coriander", "Rice", "Noodles", "Egg", "Milk", "Butter",
    "Carrot", "Potato", "Celery", "Chili", "Soy Sauce", "Fish Sauce", "Coconut Milk"
]

steps_list = [
    "Chop all the vegetables.",
    "Heat oil in a pan.",
    "Add onions and garlic, sauté until fragrant.",
    "Add protein and cook until browned.",
    "Stir in spices and seasonings.",
    "Add main liquid (water, stock, or coconut milk).",
    "Simmer until cooked through.",
    "Taste and adjust seasoning.",
    "Serve hot with garnish."
]

class Command(BaseCommand):
    help = "Seed the database with 50 recipes"

    def handle(self, *args, **kwargs):
        for _ in range(50):
            recipe = Recipe.objects.create(
                title=random.choice(titles),
                author=f"Chef {random.choice(['John', 'Anna', 'Ali', 'Maya', 'David', 'Siti'])}",
                time=f"{random.randint(10, 90)} min",
                description="This is a delicious recipe that you will love.",
                image=None  # Leave blank, or set a default if you want
            )

            # Add ingredients
            for _ in range(5):
                Ingredient.objects.create(
                    recipe=recipe,
                    name=random.choice(ingredients_list),
                    quantity=f"{random.randint(1, 500)}g"
                )

            # Add steps
            for idx in range(5):
                RecipeStep.objects.create(
                    recipe=recipe,
                    step_number=idx + 1,
                    description=random.choice(steps_list)
                )

        self.stdout.write(self.style.SUCCESS("✅ Successfully seeded 50 recipes"))
        self.stdout.write("You can now run the server and test the API with these recipes.")
        self.stdout.write("Use the Django admin or API to view and manage the recipes.")
        self.stdout.write("Enjoy cooking and testing your application!")