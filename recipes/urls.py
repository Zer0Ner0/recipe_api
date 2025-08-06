from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    RecipeViewSet, IngredientViewSet, StepViewSet,
    ReviewViewSet, NotificationViewSet, SavedRecipeViewSet
)
from . import views

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipe')
router.register(r'ingredients', IngredientViewSet, basename='ingredient')
router.register(r'steps', StepViewSet, basename='step')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'notifications', NotificationViewSet, basename='notification')
router.register(r'saved', SavedRecipeViewSet, basename='saved')


urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('add/', views.recipe_add, name='recipe_add'),
    path('edit/<int:pk>/', views.recipe_edit, name='recipe_edit'),
    path('delete/<int:pk>/', views.recipe_delete, name='recipe_delete'),
] + router.urls  #  This adds all API endpoints to the list
