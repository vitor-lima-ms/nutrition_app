from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import ListView, FormView
from django.http import HttpResponse


from datetime import datetime
import plotly.graph_objects as go

from goal.models import Goal
from meal.models import Meal
from meal.myForms import FormatForm, SearchMeal
from meal.admin import MealResource

# Create your views here.

class Index(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meals'] = Meal.objects.all()
        context['form'] = SearchMeal()
        return context


def search_by_date(request):
    if request.method == 'POST':
        form = SearchMeal(request.POST)

        if form.is_valid():
            date = form.cleaned_data['datetime']
            meals = Meal.objects.filter(datetime__date=date)
            context = {
                'meals': meals,
                'date': date,
            }
            return render(request, 'search_by_date.html', context)
    
    return redirect('meal:home')

class EditMeal(UpdateView):
    model = Meal
    fields = ['meal_name', 'protein', 'carbs', 'fat', 'calories', 'water']
    template_name = 'edit_meal.html'
    success_url = reverse_lazy('meal:home')

class DeleteMeal(DeleteView):
    model = Meal
    template_name = 'delete_meal.html'
    success_url = reverse_lazy('meal:home')

class MealDownload(ListView, FormView):
    model = Meal
    template_name = 'download_csv.html'
    form_class = FormatForm    

    def post(self, request, **kwargs):
        qs = Meal.objects.all()
        dataset = MealResource().export(qs)

        format = request.POST.get('format')

        if format == 'csv':
            formatedDataset = dataset.csv
        elif format == 'json':
            formatedDataset = dataset.json
        
        response = HttpResponse(formatedDataset, content_type=f'{format}')
        response['Content-Disposition'] = f'attachment; filename=posts.{format}'

        return response

class CreateMeal(CreateView):
    model = Meal
    fields = ['meal_name', 'protein', 'carbs', 'fat', 'calories', 'water']
    template_name = 'create_meal.html'
    success_url = reverse_lazy('meal:home')

def daily_summary(request):
    meals = Meal.objects.filter(datetime__date=datetime.now().date())

    total_protein = 0
    total_carbs = 0
    total_fat = 0
    total_calories = 0
    total_water = 0
    for meal in meals:
        total_protein += meal.protein
        total_carbs += meal.carbs
        total_fat += meal.fat
        total_calories += meal.calories
        total_water += meal.water
    
    goal = Goal.objects.last()

    fig_protein = go.Figure(go.Indicator(
        mode='gauge+number',
        value=total_protein,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Proteínas (g)"},
        gauge={'axis': {'range': [None, goal.protein_goal]}}
    ))

    chart_protein = fig_protein.to_html()

    fig_carbs = go.Figure(go.Indicator(
        mode='gauge+number',
        value=total_carbs,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Carboidratos (g)"},
        gauge={'axis': {'range': [None, goal.carbs_goal]}}
    ))

    chart_carbs = fig_carbs.to_html()

    fig_fat = go.Figure(go.Indicator(
        mode='gauge+number',
        value=total_fat,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Gorduras (g)"},
        gauge={'axis': {'range': [None, goal.fat_goal]}}
    ))

    chart_fat = fig_fat.to_html()

    fig_calories = go.Figure(go.Indicator(
        mode='gauge+number',
        value=total_calories,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Calorias (kcal)"},
        gauge={'axis': {'range': [None, goal.calories_goal]}}
    ))

    chart_calories = fig_calories.to_html()

    fig_water = go.Figure(go.Indicator(
        mode='gauge+number',
        value=total_water,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Água (mL)"},
        gauge={'axis': {'range': [None, goal.water_goal]}, 'bar': {'color': "darkblue"}}
    ))

    chart_water = fig_water.to_html()
    

    context = {
        'total_protein': total_protein,
        'total_carbs': total_carbs,
        'total_fat': total_fat,
        'total_calories': total_calories,
        'total_water': total_water,
        'date': datetime.now().date(),
        'goal': goal,
        'chart_protein': chart_protein,
        'chart_carbs': chart_carbs,
        'chart_fat': chart_fat,
        'chart_calories': chart_calories,
        'chart_water': chart_water,
    }

    return render(request, 'daily_summary.html', context)