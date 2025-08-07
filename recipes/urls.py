from django.shortcuts import redirect
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    RecipeViewSet, IngredientViewSet, StepViewSet,
    ReviewViewSet, NotificationViewSet, SavedRecipeViewSet
)
from . import views

# DRF router
router = DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipe')
router.register(r'ingredients', IngredientViewSet, basename='ingredient')
router.register(r'steps', StepViewSet, basename='step')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'notifications', NotificationViewSet, basename='notification')
router.register(r'saved', SavedRecipeViewSet, basename='saved')

urlpatterns = [
    # Admin HTML views
     path('admin/', lambda request: redirect('recipe_list')),
    path('admin/recipes/', views.recipe_list, name='recipe_list'),
    path('admin/recipes/add/', views.recipe_add, name='recipe_add'),
    path('admin/recipes/edit/<int:pk>/', views.recipe_edit, name='recipe_edit'),
    path('admin/recipes/delete/<int:pk>/', views.recipe_delete, name='recipe_delete'),

    # API endpoints under /api/v1/
    path('api/v1/', include(router.urls)),
]
