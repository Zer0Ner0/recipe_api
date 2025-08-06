from django.forms import inlineformset_factory
from rest_framework import viewsets, mixins, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Recipe, Ingredient, Step, Review, Notification, SavedRecipe
from .serializers import (
    IngredientSerializer, StepSerializer, ReviewSerializer,
    NotificationSerializer, SavedRecipeSerializer,
    RecipeListSerializer, FullRecipeSerializer
)
from .forms import RecipeForm, IngredientFormSet, RecipeStepFormSet
from django.shortcuts import render, get_object_or_404, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .filters import RecipeFilter  #  use your custom filter

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('-created_at')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'description']
    filterset_class = RecipeFilter
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return FullRecipeSerializer
        return RecipeListSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by('-created_at')
    serializer_class = NotificationSerializer

    @action(detail=True, methods=['post'])
    def mark_read(self, request, pk=None):
        notification = self.get_object()
        notification.is_read = True
        notification.save()
        return Response({'status': 'marked as read'})

    @action(detail=True, methods=['post'])
    def mark_unread(self, request, pk=None):
        notification = self.get_object()
        notification.is_read = False
        notification.save()
        return Response({'status': 'marked as unread'})

class SavedRecipeViewSet(viewsets.ModelViewSet):
    queryset = SavedRecipe.objects.all()
    serializer_class = SavedRecipeSerializer

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

def recipe_add(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form})

def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(request.POST or None, request.FILES or None, instance=recipe)
    ingredient_formset = IngredientFormSet(request.POST or None, instance=recipe, prefix='ingredients')
    step_formset = RecipeStepFormSet(request.POST or None, instance=recipe, prefix='steps')

    if form.is_valid() and ingredient_formset.is_valid() and step_formset.is_valid():
        form.save()
        ingredient_formset.save()
        step_formset.save()
        return redirect('recipe_list')

    return render(request, 'recipe_form.html', {
        'form': form,
        'ingredient_formset': ingredient_formset,
        'step_formset': step_formset,
    })

def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect('recipe_list')
    return render(request, 'recipe_confirm_delete.html', {'recipe': recipe})
