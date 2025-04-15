from django.shortcuts import render
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from datetime import datetime

from meal.models import Meal
from goal.models import Goal

# Create your views here.

class UpdateGoal(UpdateView):
    model = Goal
    template_name = 'create_goal.html'
    fields = ['protein_goal', 'carbs_goal', 'fat_goal', 'calories_goal', 'water_goal']
    success_url = reverse_lazy('meal:index')