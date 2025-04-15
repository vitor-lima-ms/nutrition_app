from django.contrib import admin

from .models import Meal
from import_export import resources

# Register your models here.

class MealResource(resources.ModelResource):
    class Meta:
        model = Meal
        fields = ('meal_name', 'protein', 'carbs', 'fat', 'calories', 'water', 'datetime')

admin.site.register(Meal)